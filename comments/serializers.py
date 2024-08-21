from rest_framework import serializers
from .models import Comment, GeneralComment
from account.serializers import UserGetSerializer

class CommentSerializer(serializers.ModelSerializer):
 
 class Meta:
  model = Comment
  fields = '__all__'

class CommentGetSerializer(serializers.ModelSerializer):

 to_user = UserGetSerializer()
 class Meta:
  model = Comment
  fields = '__all__'

class GeneralCommentSerializer(serializers.ModelSerializer):

 class Meta:
  model = GeneralComment
  fields = '__all__'

