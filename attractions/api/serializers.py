from rest_framework.serializers import ModelSerializer

from attractions.models import Attractions


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attractions
        fields = ['id', 'name', 'description', 'opening_hours', 'minimum_age']
