from django.db import models
from account.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class Comment(models.Model):

 content = models.TextField()
 to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
 level_of_satsfaction = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
 ticket = models.CharField(max_length=10, blank=False, null=False, default=123)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 
 def clean(self):
        # Get the current time
  now = timezone.now()

        # Check if any comments with the same ticket number exist within the last 24 hours
  recent_comments = Comment.objects.filter(
   ticket=self.ticket,
   created_at__gte=now - timezone.timedelta(hours=24)
  )

  if recent_comments.exists():
   raise ValidationError("The ticket number must be unique within 24 hours.")
 def save(self, *args, **kwargs):
  # Call the clean method to enforce the validation
  self.clean()
  super().save(*args, **kwargs)

 def __str__(self):
  return f"Comment by {self.to_user} on {self.created_at}"
