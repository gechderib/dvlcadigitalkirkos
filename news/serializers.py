from rest_framework import serializers
from .models import News, OfficeDirection, UserObligation, TicketAnnouncement
from django.core.exceptions import ValidationError


class NewsSerializer(serializers.ModelSerializer):

 class Meta:
  model = News
  fields = ['id', 'title', 'content', 'image', 'author', 'news_type', 'created_at', 'updated_at']


class OfficeDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeDirection
        fields = '__all__'

class UserObliqueDirectionSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = UserObligation
      fields = '__all__'



# class TicketAnouncementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TicketAnnouncement
#         fields = '__all__'
        
class TicketAnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAnnouncement
        fields = '__all__'

    def validate(self, data):
        current_ticket_number = data['current_ticket_number']
        last_ticket_number = data['last_ticket_number']
        
        # Ensure current_ticket_number is less than last_ticket_number
        if int(current_ticket_number) >= int(last_ticket_number):
            raise ValidationError("The current ticket number must be less than the last ticket number.")
        
        # Get the most recent last_ticket_number from the database
        last_ticket = TicketAnnouncement.objects.order_by('-updated_at').first()
        if last_ticket and int(last_ticket_number) <= int(last_ticket.last_ticket_number):
            raise ValidationError("The last ticket number must be greater than the previously added last ticket number.")
        
        return data
