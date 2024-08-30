from .models import CustomUser
from .serializers import UserCreateSerializer, UserGetSerializer, UserLoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,authenticate
from commons.permission import IsSelfOrReadOnly, IsAdmin, IsSuperUser
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.views import APIView

from cloudinary.uploader import upload


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateViewSet(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsSuperUser]

    def create(self, request, *args, **kwargs):
        print("--------------------------------")
        print(request.data)
        print("--------------------------------")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("99999999999999999999999999999")
            images = request.FILES.getlist('profile_pic')
            item_folder = "item_folder"

            print(images)

            if images:
                result = upload(images[0], folder=item_folder)
                image_url = result['secure_url']
                print("image_url: " + image_url)
            else:
                print("No image")
                image_url = None 
            print(image_url)
            user = CustomUser(
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                phone_number=serializer.validated_data['phone_number'],
                profile_pic=image_url,
                role=serializer.validated_data['role'],
                window_number=serializer.validated_data['window_number'] 
            )
            print(user)
            user.set_password(serializer.validated_data['password'])
            user.save()
            print("000-------------------------------- 000")

            return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            print ('User creation failed')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@method_decorator(csrf_exempt, name="dispatch")
class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserGetSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    
    
@method_decorator(csrf_exempt, name="dispatch")
class UserLoginApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        print("User login ********************************")
        serializer = self.get_serializer(data=request.data)
        # serializer = UserLoginSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            print(phone_number, password)
            # Use Django's authenticate method
            user = authenticate(request, phone_number=phone_number, password=password)
            print(user)

            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'detail': 'User successfully logged in',
                    'token': token.key,
                    'created': created
                }, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("--------------------------------")
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def userLogin(request):
    print("User login ********************************")
        # serializer = self.get_serializer(data=request.data)
    serializer = UserLoginSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']
        print(phone_number, password)
        # Use Django's authenticate method
        user = authenticate(request, phone_number=phone_number, password=password)
        print(user)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'detail': 'User successfully logged in',
                'token': token.key,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "role": user.role,
                'created': created
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffUserListView(generics.ListAPIView):
    serializer_class = UserGetSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(role__in=['user1', 'user2', 'user3', 'user4'])


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userLogout(request):
 request.auth.delete()
 return Response({'message':"Successfly logged out"}, status=status.HTTP_200_OK)



class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        user_data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "role": user.role
        }
        return Response(user_data)

