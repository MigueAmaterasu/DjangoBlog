from unicodedata import category
from django.db import models
from users.models import User
from django.db.models import SET_NULL
from categories.models import Category



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    miniature = models.ImageField(upload_to = 'post/images/')
    create_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL,null=True)

