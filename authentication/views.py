import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView as SocialLoginView
from rest_framework.permissions import IsAuthenticated
from allauth.account.views import LogoutView as AllAuthLogoutView

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return JsonResponse({'message': 'Passwords do not match'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'message': 'User created successfully'}, status=201)
    
    # Handling other HTTP methods
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # Existing POST method handling
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    elif request.method == 'GET':
        # Handle GET requests
        return JsonResponse({'message': 'GET request not supported for login'}, status=405)

class CustomLogoutView(AllAuthLogoutView):
    def post(self, *args, **kwargs):
        return super(CustomLogoutView, self).post(self.request, *args, **kwargs)
