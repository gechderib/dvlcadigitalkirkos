from django.db import models

SERVICE_TYPE = (
    ("driver", "DRIVER"),
    ("vehicle", "VEHICLE"),
)
class DriverAndVehicleStandards(models.Model):
 order_number = models.IntegerField(null=False,blank=False)
 service_name = models.TextField(null=False, blank=False, unique=True)
 service_time = models.IntegerField(null=False, blank=False)
 service_quality = models.IntegerField(null=False, blank=False)
 service_type = models.CharField(max_length=10, choices=SERVICE_TYPE, null=False, blank=False)
 
 def __str__(self) -> str:
  return f'{self.service_name}'
 

class StandardPrerequisites(models.Model):
 standard = models.ForeignKey(DriverAndVehicleStandards, on_delete=models.CASCADE, related_name="prerequisites")
 description = models.TextField(null=False, blank=False)
 