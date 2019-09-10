from rest_framework.viewsets import ModelViewSet

from core.models import TouristSpots

from core.api.serializers import TouristSpotSerializer


class TouristSpotViewSet(ModelViewSet):
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        return TouristSpots.objects.filter(approved=True)
