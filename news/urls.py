from django.urls import path
from .views import NewsCreateAPIView, NewsDestroyAPIView, NewsListAPIView, NewsUpdateAPIView, NewsRetrieveAPIView, OfficeDirectionListAPIView, UserObliqueDirectionListAPIView, TicketAnnouncementStreamView, TicketCreateAPIView, TicketListAPIView, TicketRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("create/", NewsCreateAPIView.as_view(), name="news_create"),
    path("update/<int:pk>/", NewsUpdateAPIView.as_view(), name="news_update"),
    path("get/<int:pk>/", NewsRetrieveAPIView.as_view(), name="news_retrieve"),
    path("delete/<int:pk>/", NewsDestroyAPIView.as_view(), name="news_destroy"),
    path("all/", NewsListAPIView.as_view(), name="news_list"),

    # office direction urls
    path("office/", OfficeDirectionListAPIView.as_view(), name="office_direction_list"),

    # user obligation

    path("obligations/", UserObliqueDirectionListAPIView.as_view(), name="obligations_list"),

    # streaming view
    
    path('ticket-announcement-stream/', TicketAnnouncementStreamView.as_view(), name='ticket-announcement-stream'),
    path('ticket-announcement-stream/create', TicketCreateAPIView.as_view(), name='ticket-announcement-create'),
    path('ticket-announcement-stream/all/', TicketListAPIView.as_view(), name='ticket-announcement-all'),
    path('ticket-announcement-stream/<int:pk>/', TicketListAPIView.as_view(), name='ticket-announcement-all'),

]
