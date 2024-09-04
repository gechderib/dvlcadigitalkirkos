from .models import News, OfficeDirection, UserObligation, TicketAnnouncement
from .serializers import NewsSerializer, OfficeDirectionSerializer, UserObliqueDirectionSerializer, TicketAnouncementSerializer, NewsGetSerializer
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

from cloudinary.uploader import upload
from rest_framework.response import Response
from rest_framework import status

@method_decorator(csrf_exempt, name="dispatch")
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsGetSerializer
    permission_classes = [AllowAny]


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            images = request.FILES.getlist('image')
            item_folder = "item_folder"

            if images:
                result = upload(images[0], folder=item_folder)
                image_url = result['secure_url']
                print("image_url: " + image_url)
            else:
                print("No image")
                image_url = None 
            print(image_url)
            news = News(
                title=serializer.validated_data['title'],
                content=serializer.validated_data['content'],
                news_type=serializer.validated_data['news_type'],
                image=image_url,
                author=self.request.user,
            )
            news.save()

            return Response({'detail': 'News created successfully'}, status=status.HTTP_201_CREATED)
        else:
            print ('News creation failed')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    permission_classes = [IsAuthenticated]

@method_decorator(csrf_exempt, name="dispatch")
class NewsDestroyAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# office derection view
class OfficeDirectionCreateAPIView(CreateAPIView):
    queryset = OfficeDirection.objects.all()
    serializer_class = OfficeDirectionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



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
    permission_classes = [IsAuthenticated]
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





