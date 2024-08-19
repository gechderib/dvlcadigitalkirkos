from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):

 list_display = (
  'id',
  'phone_number',
  'first_name',
  'last_name',
  'role',
  'is_active'
 )

admin.site.register(CustomUser, CustomUserAdmin)