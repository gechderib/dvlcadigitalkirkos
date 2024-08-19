from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):

 list_display = (
  'id',
  'content',
  'to_user',
  'level_of_satsfaction',
  'created_at',
  'updated_at'
  )
    

admin.site.register(Comment, CommentAdmin)