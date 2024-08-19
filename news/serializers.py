from rest_framework import serializers
from .models import News, OfficeDirection, UserObligation


class NewsSerializer(serializers.ModelSerializer):

 class Meta:
  model = News
  fields = ['id', 'title', 'content', 'image', 'author', 'news_type', 'created_at', 'updated_at']


class OfficeDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeDirection
        fields = '__all__'

class UserObliqueDirectionSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = UserObligation
      fields = '__all__'


