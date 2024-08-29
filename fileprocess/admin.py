from django.contrib import admin
from .models import FileProcess
from .models import ServiceAvailability
# Register your models here.


admin.site.register(FileProcess)
admin.site.register(ServiceAvailability)