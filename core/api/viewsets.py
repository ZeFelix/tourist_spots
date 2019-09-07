from rest_framework.viewsets import ModelViewSet

from core.models import TouristSpots

from core.api.serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    queryset = TouristSpots.objects.all()
    serializer_class = TouristSpotSerializer
