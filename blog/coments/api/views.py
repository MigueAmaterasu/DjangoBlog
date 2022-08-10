from rest_framework.viewsets import ModelViewSet
from coments.models import Comment
from coments.api.serializers import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from coments.api.permissions import IsOwnerOrReadOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer    
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter]
    ordering = ['-created_at']
    filterset_fields = ['post']


