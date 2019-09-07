from rest_framework.viewsets import ModelViewSet

from evaluations.api.serializers import EvaluationSerializer
from evaluations.models import Evaluations


class EvaluationViewSet(ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationSerializer
