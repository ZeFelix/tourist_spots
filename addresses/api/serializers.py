from rest_framework.serializers import ModelSerializer

from addresses.models import Addresses


class AddressesSerializer(ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['id', 'address_one', 'address_two', 'city', 'state', 'lat', 'long']
