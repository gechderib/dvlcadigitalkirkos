from django.urls import path
from .views import UserCreateViewSet, UserDetailViewSet, UserLoginApiView, userLogout


urlpatterns = [
    path("register/", UserCreateViewSet.as_view(), name="register"),
    path("<int:pk>/", UserDetailViewSet.as_view(), name="user"),
    path("login/", UserLoginApiView.as_view(), name="login"),
    path("logout/", userLogout, name="logout"),
]
