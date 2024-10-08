from django.urls import path
from .views import FileProcessCreateAPIView, FileProcessListAPIView,FileProcessFilteredView, FileProcessUpdateAPIView,FileProcessRetrieveAPIView, FileProcessDestroyAPIView,FileProcessDateRangeReportAPIView, FileProcessStatusReportAPIView, ServiceAvailabilityView, FileProcessDetailView

urlpatterns = [
 
    path('create/', FileProcessCreateAPIView.as_view(), name='file-create'),
    path('all/', FileProcessListAPIView.as_view(), name='file-list'),
    path('update/<int:pk>/', FileProcessUpdateAPIView.as_view(), name='file_update'),
    path('delete/<int:pk>/', FileProcessDestroyAPIView.as_view(), name='fiel_delete'),
    path('detail/<int:pk>/', FileProcessRetrieveAPIView.as_view(), name='fiel_detail'),
    path('report/date-range/', FileProcessDateRangeReportAPIView.as_view(), name='file-process-date-range-report'),
    path('report/status/', FileProcessStatusReportAPIView.as_view(), name='file-process-status-report'),
    path('service-availability/', ServiceAvailabilityView.as_view(), name='service-availability'),
    path('fileprocess/<str:file_serial_number>/', FileProcessDetailView.as_view(), name='fileprocess-detail'),
    path('filter/', FileProcessFilteredView.as_view(), name='fileprocess-filter'),

]