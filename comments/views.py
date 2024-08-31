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
from account.models import CustomUser
from account.serializers import UserGetSerializer
from commons.permission import IsSuperUser, IsAdmin, IsSelfOrReadOnly
from django.utils.timezone import now, timedelta
from django.db.models import Avg
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


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


class SatisfactionView(APIView):
    def get(self, request):
        today = now()
        start_of_week = today - timedelta(days=today.weekday())

        # Filter comments from the start of the week to now
        weekly_comments = Comment.objects.filter(created_at__gte=start_of_week)

        # Group by user and calculate the average level of satisfaction for the week
        weekly_user_satisfaction = weekly_comments.values('to_user').annotate(avg_satisfaction=Avg('level_of_satisfaction')).order_by('-avg_satisfaction')

        # Get the overall average level of satisfaction for each user
        overall_user_satisfaction = Comment.objects.values('to_user').annotate(avg_satisfaction=Avg('level_of_satisfaction')).order_by('-avg_satisfaction')

        # Serialize the data with user details
        weekly_data = []
        for entry in weekly_user_satisfaction:
            user = CustomUser.objects.get(id=entry['to_user'])
            entry_data = {
                'user': UserGetSerializer(user).data,
                'average_satisfaction': entry['avg_satisfaction']
            }
            weekly_data.append(entry_data)

        overall_data = []
        for entry in overall_user_satisfaction:
            user = CustomUser.objects.get(id=entry['to_user'])
            entry_data = {
                'user': UserGetSerializer(user).data,
                'average_satisfaction': entry['avg_satisfaction']
            }
            overall_data.append(entry_data)

        response_data = {
            'weekly_user_satisfaction': weekly_data,
            'overall_user_satisfaction': overall_data
        }

        return Response(response_data)




class UserCommentsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the user ID from the query parameters
        print(request.user.id)
        print("the above value")
        user_id = request.user.id
        
        # Validate that the user ID was provided
        if not user_id:
            return Response({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the user object or return a 404 if the user doesn't exist
        user = get_object_or_404(CustomUser, id=user_id)
        
        # Filter comments where the specified user is the 'to_user'
        comments = Comment.objects.filter(to_user=user)
        
        # Serialize the comments
        serializer = CommentGetSerializer(comments, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
