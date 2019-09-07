from rest_framework.serializers import ModelSerializer

from evaluations.models import Evaluations


class EvaluationSerializer(ModelSerializer):
    class Meta:
        model = Evaluations
        fields = ['id', 'user', 'comment', 'note', 'date']
