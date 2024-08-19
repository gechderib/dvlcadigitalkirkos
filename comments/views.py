from .models import Comment
from .serializers import CommentSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from commons.permission import IsSuperUser, IsAdmin, IsSelfOrReadOnly


@method_decorator(csrf_exempt, name="dispatch")
class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission = [AllowAny]
    


@method_decorator(csrf_exempt, name="dispatch")
class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    



@method_decorator(csrf_exempt, name="dispatch")
class CommentDetailApiViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser,]
    lookup_field = 'pk'





    



