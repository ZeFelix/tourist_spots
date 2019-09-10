from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from attractions.api.serializers import AttractionSerializer
from attractions.models import Attractions


class AttractionViewSet(ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
