from .models import FileProcess
from .serializers import FileProcessSerializer, FileProcessGetSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import FileProcess
from datetime import datetime

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from commons.permission import IsSuperUser, IsAdmin, IsSelfOrReadOnly

from .models import ServiceAvailability
from .serializers import ServiceAvailabilitySerializer


class FileProcessCreateAPIView(CreateAPIView):
    queryset = FileProcess.objects.all()
    serializer_class = FileProcessSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        print("______________________________")
        # Get the logged-in user from the request and pass it as file_created_by
        serializer.save(file_created_by=self.request.user)


class FileProcessListAPIView(ListAPIView):
    # queryset = FileProcess.objects.all()
    serializer_class = FileProcessGetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = FileProcess.objects.all()
        file_status = self.request.query_params.get('file_status')
        if file_status:
            queryset = queryset.filter(file_status=file_status)
        return queryset
    



class FileProcessRetrieveAPIView(RetrieveAPIView):
    queryset = FileProcess.objects.all()
    serializer_class = FileProcessGetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'


class FileProcessUpdateAPIView(UpdateAPIView):
    queryset = FileProcess.objects.all()
    serializer_class = FileProcessSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class FileProcessDestroyAPIView(DestroyAPIView):
    queryset = FileProcess.objects.all()
    serializer_class = FileProcessSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class FileProcessDateRangeReportAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        file_status = request.query_params.get('file_status')
        
        
        if file_status:
            report = FileProcess.objects.filter(created_at__range=(start_date, end_date), file_status=file_status)
        elif start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
            report = FileProcess.objects.filter(created_at__range=(start_date, end_date))
        else:
            report = FileProcess.objects.all()

        serializer = FileProcessGetSerializer(report, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class FileProcessStatusReportAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        report = FileProcess.objects.values('file_status').annotate(count=Count('file_status')).order_by('file_status')
        return Response(report, status=status.HTTP_200_OK)



class ServiceAvailabilityView(APIView):
    def get(self, request):
        try:
            service_availability = ServiceAvailability.objects.first()
            if not service_availability:
                return Response({'error': 'Service availability not set.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ServiceAvailabilitySerializer(service_availability)
            return Response(serializer.data)
        except ServiceAvailability.DoesNotExist:
            return Response({'error': 'Service availability not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        service_availability, created = ServiceAvailability.objects.get_or_create(id=1)
        serializer = ServiceAvailabilitySerializer(service_availability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


