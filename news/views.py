from .models import News, OfficeDirection, UserObligation, TicketAnnouncement
from .serializers import NewsSerializer, OfficeDirectionSerializer, UserObliqueDirectionSerializer, TicketAnouncementSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from commons.permission import IsSuperUser, IsAdmin, IsSelfOrReadOnly


from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import time

@method_decorator(csrf_exempt, name="dispatch")
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


@method_decorator(csrf_exempt, name="dispatch")
class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]

@method_decorator(csrf_exempt, name="dispatch")
class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


@method_decorator(csrf_exempt, name="dispatch")
class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]

@method_decorator(csrf_exempt, name="dispatch")
class NewsDestroyAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]


# office derection view


class OfficeDirectionCreateAPIView(CreateAPIView):
    queryset = OfficeDirection.objects.all()
    serializer_class = OfficeDirectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]



class OfficeDirectionListAPIView(ListAPIView):
    queryset = OfficeDirection.objects.all()
    serializer_class = OfficeDirectionSerializer
    permission_classes = [AllowAny]


class OfficeDirectionRetrieveAPIView(RetrieveAPIView):
    queryset = OfficeDirection.objects.all()
    serializer_class = OfficeDirectionSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


class OfficeDirectionUpdateAPIView(UpdateAPIView):
    queryset = OfficeDirection.objects.all()
    serializer_class = OfficeDirectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_field = 'pk'


# user oblicaion view

class UserObliqueDirectionListAPIView(ListAPIView):
    queryset = UserObligation.objects.all()
    serializer_class = UserObliqueDirectionSerializer
    permission_classes = [AllowAny]




@method_decorator(csrf_exempt, name='dispatch')
class TicketAnnouncementStreamView(View):
    def get(self, request, *args, **kwargs):
        def event_stream():
            while True:
                ticket = TicketAnnouncement.objects.last()
                if ticket:
                    yield f"data: {{\"current_ticket_number\": \"{ticket.current_ticket_number}\", \"last_ticket_number\": \"{ticket.last_ticket_number}\"}}\n\n"
                time.sleep(5)  # Update every hour

        response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
        return response



class TicketCreateAPIView(CreateAPIView):
    queryset = TicketAnnouncement.objects.all()
    serializer_class = TicketAnouncementSerializer


class TicketListAPIView(ListAPIView):
    queryset = TicketAnnouncement.objects.all()
    serializer_class = TicketAnouncementSerializer


class TicketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TicketAnnouncement.objects.all()
    serializer_class = TicketAnouncementSerializer
    lookup_field = 'pk'





