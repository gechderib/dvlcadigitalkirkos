from django.urls import path
from .views import UserCreateViewSet, UserDetailViewSet, UserLoginApiView, userLogout, userLogin, StaffUserListView


urlpatterns = [
    path('register/', UserCreateViewSet.as_view(), name="register"),
    path('<int:pk>/', UserDetailViewSet.as_view(), name="user"),
    path('login/', userLogin, name="login"),
    path('logout/', userLogout, name="logout"),
    path('staff-users/', StaffUserListView.as_view(), name='staff-user-list'),

]

