# Serializers define the API representation.
from rest_framework.serializers import ModelSerializer

from core.models import TouristSpots


class TouristSpotSerializer(ModelSerializer):
    class Meta:
        model = TouristSpots
        fields = ['id', 'name', 'description', 'approved']
