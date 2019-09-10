from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from evaluations.api.serializers import EvaluationSerializer
from evaluations.models import Evaluations


class EvaluationViewSet(ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
