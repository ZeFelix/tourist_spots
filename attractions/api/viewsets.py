from rest_framework.viewsets import ModelViewSet

from attractions.api.serializers import AttractionsSerializer
from attractions.models import Attractions


class AttractionsViewSet(ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer