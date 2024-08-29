from rest_framework import serializers
from .models import FileProcess
from account.serializers import UserGetSerializer
from .models import ServiceAvailability


class FileProcessSerializer(serializers.ModelSerializer):

 class Meta:
  model = FileProcess
  fields = ['file_serial_number', 'file_name','file_content','file_status','created_at','updated_at']


class FileProcessGetSerializer(serializers.ModelSerializer):

 file_created_by = UserGetSerializer()
 class Meta:
  model = FileProcess
  fields = '__all__'



class ServiceAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAvailability
        fields = ['is_available']
