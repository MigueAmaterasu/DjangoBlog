from pyexpat import model
from django.db import models
from users.models import User
from django.db.models import CASCADE
from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)
    

