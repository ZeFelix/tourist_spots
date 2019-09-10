from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from core.models import TouristSpots

from core.api.serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']

    def get_queryset(self):
        return TouristSpots.objects.filter(approved=True)
