from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

 class Meta:
  model = Comment
  fields = ['content', 'to_user', 'level_of_satsfaction', 'created_at', 'updated_at']