from rest_framework import serializers
from .constants import CONTACT_NUMBER_SIZE


class contactNumberValidator:

    def __call__(self, contactNumber):
        if contactNumber is None:  # for not showing default error message of not null
            message = "Enter your Contact Number"
            raise serializers.ValidationError(message)

        if len(str(contactNumber)) != CONTACT_NUMBER_SIZE:  # contact number must be of desired size
            message = f"Contact Number should be of {CONTACT_NUMBER_SIZE} digits"
            raise serializers.ValidationError(message)
        return contactNumber
