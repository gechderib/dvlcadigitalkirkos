from django.urls import path
from .views import CommentCreateAPIView, CommentListAPIView, CommentDetailApiViewSet


urlpatterns = [
    path("create/", CommentCreateAPIView.as_view(), name="comment_create"),
    path("<int:pk>/", CommentDetailApiViewSet.as_view(), name="comment_detail"),
    path("all/", CommentListAPIView.as_view(), name="comment_list"),
]
