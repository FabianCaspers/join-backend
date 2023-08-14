from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, CurrentUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_data = serializer.validated_data
        user = get_user_model().objects.get(email=user_data['email'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })

        
        
class RegisterView(APIView):
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.pk,
            'email': user.email,
            # 'token': token.key
        },)
        
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    serializer = CurrentUserSerializer(request.user)
    return Response(serializer.data)