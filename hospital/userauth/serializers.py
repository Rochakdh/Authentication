from rest_framework import serializers

from django.contrib.auth import get_user_model
from .validators import contactNumberValidator

USER = get_user_model()


class customUsersDetailSearializers(serializers.ModelSerializer):
    """ Custom User Model Searilizers for Signing In Form"""

    # secondPassword is not attribute of the USER model.
    # secondPassword is defined here as write_only_field only will only be  applicable to model's attribute

    secondPassword = serializers.CharField(
        label='Confirm Password',
        allow_blank=False,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = USER
        fields = ['id', 'username', 'email', 'contactNumber', 'password', 'secondPassword']
        read_only_fields = ['id']
        validators = [contactNumberValidator()]
        extra_kwargs = {
            'password': {
                'max_length': 128,
                'style': {
                    'input_type': 'password',
                },
                'write_only': True
            },
        }

    def validate(self, data):
        """
        Checks if the password and secondPassword matches
        :param data: dictionary key,value from field,submitted data
        :return data without secondPassword key in dictionary:
        """
        password = data['password']
        confirm_password = data['secondPassword']
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Password Do Not Match")
        else:
            # Popping out secondPassword key,value as there is no attribute in model to save
            _ = data.pop('secondPassword')
        return data

    def create(self, validated_data):
        """
        Overriding create class to set hashable password of user
        :param validated_data : dictionary key,value after data from form is validated
        :return: instance of the CustomUser
        """
        password = validated_data['password']
        user = super(customUsersDetailSearializers, self).create(validated_data)
        user.set_password(password)  # converting to hashable password
        user.save()
        return user

    def update(self, instance, validated_data):
        """
            Overriding update class to set hashable password of user
            :param instance : the instace of the class that is being updated
            :param validated_data : dictionary key,value after data from form is validated
            :return: instance of the CustomUser
        """
        password = validated_data.get('password')
        user = super(customUsersDetailSearializers, self).update(instance, validated_data)
        user.set_password(password)  # converting to hashable password
        user.save()
        return user
