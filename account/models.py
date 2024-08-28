
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

 def create_user(self,phone_number, password= None,**extra_fields):
  if not phone_number:
   raise ValueError("User must have a phone number")
  
  user = self.model(phone_number=phone_number, **extra_fields)
  user.set_password(password)
  user.save(using=self._db)
  return user
 
 def create_superuser(self, phone_number, password, **extra_fields):

  extra_fields.setdefault("is_staff", True)
  extra_fields.setdefault("is_superuser", True)

  if extra_fields.get("is_staff") is not True:
   raise ValueError("Super user must have staff = True")
  if extra_fields.get("is_superuser") is not True:
   raise ValueError("Super user must have is_superuser = True")
  
  return self.create_user(phone_number, password, **extra_fields)


ROLE_CHOICES = (
 ('admin', 'Admin'),
 ('staff', 'Staff'),
 ('user', 'User'),
 ('user1', 'User1'),
 ('user2', 'User2'),
 ('user3', 'User3'),
 ('user4', 'User4'),
)


class CustomUser(AbstractUser):

 first_name = models.CharField(verbose_name="First Name", max_length=255)
 last_name = models.CharField(verbose_name="Last Name", max_length=255)
 phone_number = models.CharField(verbose_name="Phone Number", max_length=15, unique=True, blank=False, null=False)
 password = models.CharField(verbose_name="Password", max_length=255, blank=False, null=False)
 role = models.CharField(verbose_name="Role", max_length=20, choices=ROLE_CHOICES, default='staff')
 profile_pic = models.ImageField(blank=True, null=True, upload_to='images/')

 def __str__(self):
  return f"{self.first_name} {self.last_name}"
 
 username = None
 email = None
 objects = UserManager()
 
 USERNAME_FIELD = 'phone_number'
 REQUIRED_FIELDS = ['first_name', "last_name", "profile_pic", "role"]

 
