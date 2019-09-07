from rest_framework.viewsets import ModelViewSet

from addresses.api.serializers import AddressesSerializer
from addresses.models import Addresses


class AddressViewSet(ModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
