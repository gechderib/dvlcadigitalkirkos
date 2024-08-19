from django.urls import path
from .views import NewsCreateAPIView, NewsDestroyAPIView, NewsListAPIView, NewsUpdateAPIView, NewsRetrieveAPIView, OfficeDirectionListAPIView, UserObliqueDirectionListAPIView


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


]
