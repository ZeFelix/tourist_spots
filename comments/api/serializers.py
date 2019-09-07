from rest_framework.serializers import ModelSerializer

from comments.models import Comments


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'comment', 'date', 'approved']