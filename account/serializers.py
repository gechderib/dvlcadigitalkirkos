from rest_framework import serializers
from .models import CustomUser
from comments.serializers import CommentSerializer

class UserCreateSerializer(serializers.ModelSerializer):

 password = serializers.CharField(write_only=True)

 class Meta:
  model = CustomUser
  fields = ['id', 'first_name', 'last_name', 'role','phone_number','password']
  extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
   user = CustomUser(**validated_data)
   return user


class UserGetSerializer(serializers.ModelSerializer):
 
 comments = CommentSerializer(many=True)
 class Meta:
  model = CustomUser
  fields = ['first_name', 'last_name','phone_number','comments']


class UserLoginSerializer(serializers.Serializer):

 password = serializers.CharField(write_only=True)
 phone_number = serializers.CharField()
