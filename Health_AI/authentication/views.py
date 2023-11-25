from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.contrib.auth import logout as django_logout

from .serializers import CustomUserSerializer, UserLoginSerializer

# API endpoint to register a new user
class RegisterUserView(APIView):
    """
    API endpoint to register a new user.
    """

    def post(self, request):
        """
        POST request to create a new user.
        """

        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API endpoint to login a user and generate JWT tokens
class LoginUserView(APIView):
    """
    API endpoint to login a user and generate JWT tokens.
    """

    def post(self, request):
        """
        POST request to login a user and generate JWT tokens.
        """

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user:
                # Generate JWT tokens for authenticated user
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Google login view using allauth
class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def get_response(self):
        # Generate JWT tokens for authenticated user
        refresh = self.token
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


# Logout view using all-auth
class LogoutView(APIView):
    """
    API endpoint to log out the user.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        POST request to log out the user.
        """

        # Logout the user using Django all-auth
        django_logout(request)

        return Response({'success': 'User logged out successfully.'}, status=status.HTTP_200_OK)

