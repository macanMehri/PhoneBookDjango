from .models import Person, Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address

        fields = (
            'id',
            'country',
            'city',
            'exact_location'
        )


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        
        address = AddressSerializer

        fields = (
            'id',
            'first_name',
            'last_name',
            'number'
        )

