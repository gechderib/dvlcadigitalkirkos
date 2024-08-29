from django.db import models
from account.models import CustomUser

FILE_STATUS = (
 ('start',"Start"),
 ('checked',"Checked"),
 ('scanned',"Scanned"),
 ('recorded',"Recorded"),
)
# Create your models here.
class FileProcess(models.Model):
 file_serial_number = models.CharField(max_length=255, null=False, blank=False, unique=True)
 file_name = models.CharField(max_length=255, null=False, blank=False)
 file_content = models.TextField(null=False, blank=False)
 file_status = models.CharField(max_length=10, choices=FILE_STATUS, default="start")
 file_created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="filesm")
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)


 def __str__(self):
  return f"{self.file_name} {self.file_content} {self.file_serial_number}"
 
class ServiceAvailability(models.Model):
    is_available = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service is {'available' if self.is_available else 'unavailable'}"




