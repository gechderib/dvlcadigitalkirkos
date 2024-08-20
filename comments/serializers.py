from rest_framework import serializers
from .models import Comment
from account.serializers import UserGetSerializer

class CommentSerializer(serializers.ModelSerializer):
 
 to_user = UserGetSerializer()
 class Meta:
  model = Comment
  fields = '__all__'
