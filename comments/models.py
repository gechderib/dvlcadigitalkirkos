from django.db import models
from account.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Comment(models.Model):

 content = models.TextField()
 to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
 level_of_satsfaction = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
 ticket = models.CharField(max_length=10, blank=False, null=False)
 ticket_img = models.ImageField(upload_to="images/", null=True, blank=True)
 window_number = models.CharField(max_length=10, blank=False, null=False)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 

 def __str__(self):
  return f"Comment by {self.to_user} on {self.created_at}"
