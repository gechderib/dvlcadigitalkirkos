from django.urls import path
from .views import CommentCreateAPIView, CommentListAPIView, CommentDetailApiViewSet, GeneralCommentListAPIView, GeneralCommentCreateAPIView, GeneralCommentDetailApiViewSet, SatisfactionView


urlpatterns = [
    path("create/", CommentCreateAPIView.as_view(), name="comment_create"),
    path("<int:pk>/", CommentDetailApiViewSet.as_view(), name="comment_detail"),
    path("all/", CommentListAPIView.as_view(), name="comment_list"),

    path("general/create/", GeneralCommentCreateAPIView.as_view(), name="genral_comment_create"),
    path("general/<int:pk>/", GeneralCommentDetailApiViewSet.as_view(), name="general_comment_detail"),
    path("general/all/", GeneralCommentListAPIView.as_view(), name="general_comment_list"),
    path("top_three/", SatisfactionView.as_view(), name="top_three"),


]
