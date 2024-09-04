from django.db import models
from account.models import CustomUser

FILE_STATUS = (
  ('requested', "Requested"),
  ('approved', "Approved"),
  ('fileout', "FileOut"),
  ('uncheck','Unchecked'),
  ('start',"Start"),
  ('checked',"Checked"),
  ('scanned',"Scanned"),
  ('recorded',"Recorded"),
)
SERVICE_TYPE = (
   ('service1','Service one'),
   ('service2','Service Two'),
   ('service3','Service Three'),
   ('service4','Service Four'),
   )

PLATE_CODE = (
   ('plate1','plate one'),
   ('plate2','plate two'),
   ('plate3','plate three'),
   ('plate4','plate four'),
)

REGION = (
   ('aa','Addis Ababa'),
   ('et','Ethiopia'),
)

LICENSE_TYPE = (
   ('level1','Level 1'),
   ('level2','Level 2'),
   ('level3','Level 3'),
   ('level4','Level 4'),
   ('level5','Level 5'),
   ('level6','Level 6'),
   
)

SERVICE_FOR = (
   ('driver','Driver'),
   ('vehicle','Vehicle'),
)


# Create your models here.
class FileProcess(models.Model):
 file_serial_number = models.CharField(max_length=255, null=False, blank=False, unique=True)

 file_name = models.CharField(max_length=255, null=True, blank=True)
 file_content = models.TextField(null=False, blank=True)

 file_status = models.CharField(max_length=10, choices=FILE_STATUS, default="start")
 file_created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="filesm")

 service_for = models.CharField(max_length=255, choices=SERVICE_FOR, null=True, blank=True)
 service_type = models.CharField(max_length=255, choices=SERVICE_TYPE, null=True, blank=True)
 plate_code = models.CharField(max_length=255, choices=PLATE_CODE, null=True, blank=True)
 region = models.CharField(max_length=255, choices=REGION, null=True, blank=True)
 owner_name = models.CharField(max_length=255, null=True, blank=True)

 driver_license_number = models.CharField(max_length=255, null=True, blank=True)
 license_type= models.CharField(max_length=255, choices=LICENSE_TYPE, null=True, blank=True)

 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)


 def __str__(self):
  return f"{self.file_name} {self.file_content} {self.file_serial_number}"
 
class ServiceAvailability(models.Model):
    is_available = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service is {'available' if self.is_available else 'unavailable'}"




