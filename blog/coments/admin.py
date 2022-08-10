from django.contrib import admin
from coments.models import Comment


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['content','user','post','created_at']
    
