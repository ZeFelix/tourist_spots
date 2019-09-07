from rest_framework.viewsets import ModelViewSet

from attractions.api.serializers import AttractionSerializer
from attractions.models import Attractions


class AttractionViewSet(ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionSerializer