from .models import DriverAndVehicleStandards, StandardPrerequisites
from rest_framework import serializers

class StandardPrerequisitesSerializer(serializers.ModelSerializer):
  class Meta:
    model = StandardPrerequisites
    fields = '__all__'

class DriverAndVehicleStandardsSerializer(serializers.ModelSerializer):
  prerequisites = StandardPrerequisitesSerializer(many=True, read_only=True)

  class Meta:
    model = DriverAndVehicleStandards
    fields = '__all__'
