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
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .models import PasswordReset
from django.utils.encoding import force_str



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





@api_view(['POST'])
def send_reset_email(request):
    email = request.data.get('email')
    user = User.objects.get(email=email)
    
    # Generate Token
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    
    # Safe Token
    PasswordReset.objects.create(user=user, token=token)
    
    # Send Mail
    mail_subject = 'Reset your password.'
    message = f"Here is your link to reset your password: https://darkjoin.fabiancaspers.com/html/reset-password.html?uid={uid}&token={token}"
    send_mail(mail_subject, message, 'fabian.caspers1308@gmail.com', [email], fail_silently=False)
    
    return Response({"message": "Email sent."})


@api_view(['POST'])
def reset_password_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        # Token is awiabled, set password
        new_password = request.data.get('password')
        user.set_password(new_password)
        user.save()
        # After use Token, delete Token
        PasswordReset.objects.filter(user=user, token=token).delete()
        return Response({"message": "Password reset successful."})
    else:
        return Response({"error": "Invalid token."}, status=400)