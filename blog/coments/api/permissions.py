from rest_framework.permissions import BasePermission
from coments.models import Comment


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)
            id_user = request.user.pk
            id_user_comment = Comment.user_id

            if id_user == id_user_comment:
                return True

            return False