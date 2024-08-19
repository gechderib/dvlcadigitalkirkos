from .models import DriverAndVehicleStandards, StandardPrerequisites
from .serializers import DriverAndVehicleStandardsSerializer, StandardPrerequisitesSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from commons.permission import IsSuperUser, IsAdmin, IsSelfOrReadOnly

@method_decorator(csrf_exempt, name="dispatch")
class ServiceCreateAPIView(generics.CreateAPIView):
    queryset = DriverAndVehicleStandards.objects.all()
    serializer_class = DriverAndVehicleStandardsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]


@method_decorator(csrf_exempt, name="dispatch")
class ServiceListAPIView(generics.ListAPIView):
    queryset = DriverAndVehicleStandards.objects.all()
    serializer_class = DriverAndVehicleStandardsSerializer


@method_decorator(csrf_exempt, name="dispatch")
class ServiceRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverAndVehicleStandards.objects.all()
    serializer_class = DriverAndVehicleStandardsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_field = 'pk'


# standart prerequest


class StandardPrerequisitesCreateAPIView(generics.CreateAPIView):
    queryset = StandardPrerequisites.objects.all()
    serializer_class = StandardPrerequisitesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]

class StandardPrerequisitesListAPIView(generics.ListAPIView):
    queryset = StandardPrerequisites.objects.all()
    serializer_class = StandardPrerequisitesSerializer

class StandardPrerequisitesRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StandardPrerequisites.objects.all()
    serializer_class = StandardPrerequisitesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_field = 'pk'
    
