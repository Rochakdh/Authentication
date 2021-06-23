from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import contactNumberValidator

USER = get_user_model()


class customUsersDetailSearializers(serializers.ModelSerializer):
    """ Custom User Model Searilizers for Signing Up Form"""

    secondPassword = serializers.CharField(label='Confirm Password')
    class Meta:
        model = USER
        fields = ['id', 'email', 'contactNumber', 'password', 'secondPassword']
        read_only_field = ['id']
        validators = [contactNumberValidator()]

        class Meta:
            extra_kwargs = {
                'firstPassword': {
                    'max_length': 128,
                    'style': {
                        'input_type': 'password',
                    },
                    'write_only': True
                },
                'secondPassword': {
                    'max_length': 128,
                    'style': {
                        'input_type': 'password'
                    },
                    'write_only': True
                }
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