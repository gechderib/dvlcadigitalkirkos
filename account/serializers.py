from rest_framework import serializers
from .models import CustomUser
# from comments.serializers import CommentSerializer

class UserCreateSerializer(serializers.ModelSerializer):

 password = serializers.CharField(write_only=True)
 profile_pic = serializers.ImageField(max_length=None, allow_empty_file=True, required=False)

 class Meta:
  model = CustomUser
  fields = ['id', 'first_name', 'last_name', 'role','phone_number','password','profile_pic']
  extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
   user = CustomUser(**validated_data)
   return user


class UserGetSerializer(serializers.ModelSerializer):
 
 profile_pic = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False)
#  comments = CommentSerializer(many=True)

 class Meta:
  model = CustomUser
  fields = ['id','first_name', 'last_name','phone_number','profile_pic', 'role']


class UserLoginSerializer(serializers.Serializer):

 password = serializers.CharField(write_only=True)
 phone_number = serializers.CharField()
