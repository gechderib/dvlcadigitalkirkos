from django.contrib import admin
from .models import DriverAndVehicleStandards, StandardPrerequisites

class DriverAndvehicleAdmin(admin.ModelAdmin):

 list_display = (
  'id',
  'order_number',
  'service_name',
  'service_time',
  'service_quality',
  'service_type',
 )

class StandardPrerequestAdmin(admin.ModelAdmin):
  list_display = (
  'id',
  'standard',
  'description',
  )
 


  

admin.site.register(DriverAndVehicleStandards, DriverAndvehicleAdmin)
admin.site.register(StandardPrerequisites,StandardPrerequestAdmin)
