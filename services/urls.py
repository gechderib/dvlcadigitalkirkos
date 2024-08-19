from django.urls import path
from .views import ServiceCreateAPIView, ServiceListAPIView, ServiceRetriveUpdateDestroyView, StandardPrerequisitesCreateAPIView, StandardPrerequisitesListAPIView, StandardPrerequisitesRetriveUpdateDestroy

urlpatterns = [
    path('create/', ServiceCreateAPIView.as_view(), name="create"),
    path('all/', ServiceListAPIView.as_view(), name="all"),
    path('<int:pk>/', ServiceRetriveUpdateDestroyView.as_view(), name="create"),

    # standart prerequest

    path('standart_prerequest/create/', StandardPrerequisitesCreateAPIView.as_view(), name="standart_prerequest_create"),
    path('standart_prerequest/all/', StandardPrerequisitesListAPIView.as_view(), name="standart_prerequest_all"),
    path('standart_prerequest/<int:pk>/', StandardPrerequisitesRetriveUpdateDestroy.as_view(), name="standart_prerequest_uvd")
]
