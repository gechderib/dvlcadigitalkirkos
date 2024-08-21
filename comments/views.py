from .models import Comment, GeneralComment
from .serializers import CommentSerializer, GeneralCommentSerializer, CommentGetSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone

from commons.permission import IsSuperUser, IsAdmin, IsSelfOrReadOnly


@method_decorator(csrf_exempt, name="dispatch")
class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentGetSerializer
    permission = [AllowAny]
  

@method_decorator(csrf_exempt, name="dispatch")
class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        ticket = request.data.get('ticket',)
        now = timezone.now()
        # Check if the ticket already exists
        if Comment.objects.filter(ticket=ticket, created_at__gte=now - timezone.timedelta(hours=24)).exists():
            return Response({"detail": "Ticket already commented in the las 24 hours."}, status=status.HTTP_400_BAD_REQUEST)

        # If the ticket does not exist, proceed with the creation
        return super().create(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class CommentDetailApiViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentGetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser ]
    lookup_field = 'pk'





  
@method_decorator(csrf_exempt, name="dispatch")
class GeneralCommentListAPIView(generics.ListAPIView):
    queryset = GeneralComment.objects.all()
    serializer_class = GeneralCommentSerializer
    permission = [AllowAny]
    

@method_decorator(csrf_exempt, name="dispatch")
class GeneralCommentCreateAPIView(generics.CreateAPIView):
    queryset = GeneralComment.objects.all()
    serializer_class = GeneralCommentSerializer
    permission_classes = [AllowAny]
    

@method_decorator(csrf_exempt, name="dispatch")
class GeneralCommentDetailApiViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralComment.objects.all()
    serializer_class = GeneralCommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser,]
    lookup_field = 'pk'



    



