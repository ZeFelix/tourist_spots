from rest_framework.serializers import ModelSerializer

from addresses.models import Addresses


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['id', 'address_one', 'address_two', 'city', 'state', 'lat', 'long']
