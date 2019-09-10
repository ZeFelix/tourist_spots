from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comments.api.serializers import CommentSerializer
from comments.models import Comments


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['comment']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
