from django.db import models
from account.models import CustomUser

NEWS_LEVEL = (
 ('urgent',"Urgent"),
 ('normal',"Normal"),
)
class News(models.Model):


 title = models.CharField(max_length=200)
 content = models.TextField()
 image = models.ImageField(upload_to='images/')
 author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='news')
 news_type = models.CharField(max_length=10, choices=NEWS_LEVEL)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)


# office direction modle

class OfficeDirection(models.Model):
    name = models.CharField(max_length=100)
    start_room = models.IntegerField()
    end_room = models.IntegerField()  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.start_room}-{self.end_room})"
    
    class Meta:
        ordering = ['start_room']
 
# user obligation modle
class UserObligation(models.Model):
   content = models.TextField(null=False, blank=False, unique=True)
   def __str__(self):
      return f"{self.content}"


class TicketAnnouncement(models.Model):
   ticket_number = models.CharField(max_length=10, blank=False, null=False)

   def __str__(self):
      return f"Ticket range: {self.ticket_number}"



