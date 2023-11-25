import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_auth.views import LogoutView as RestAuthLogoutView
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.views import SocialLoginView
from rest_framework.permissions import IsAuthenticated
from allauth.account.views import LogoutView as AllAuthLogoutView
from allauth.socialaccount.views import DisconnectView

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
        user.save()
        return JsonResponse({'message': 'User created successfully'}, status=201)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def process_login(self):
        get_request = self.request.GET.copy()
        get_request['process'] = True
        self.request.GET = get_request

        self.serializer.is_valid(raise_exception=True)
        login(self.request, self.user)

        
        google_account = SocialAccount.objects.get(user_id=self.user.id, provider='google')
        google_data = {
            'id': google_account.uid,
            'email': google_account.extra_data.get('email'),
            'name': google_account.extra_data.get('name'),
            
        }
        return JsonResponse({'message': 'Google login successful', 'google_data': google_data})

class CustomLogoutView(AllAuthLogoutView):
    def post(self, *args, **kwargs):
        return super(CustomLogoutView, self).post(self.request, *args, **kwargs)

class CustomDisconnectView(DisconnectView):
    def post(self, *args, **kwargs):
        return super(CustomDisconnectView, self).post(self.request, *args, **kwargs)

class CustomRestAuthLogoutView(RestAuthLogoutView):
    def post(self, *args, **kwargs):
        return super(CustomRestAuthLogoutView, self).post(self.request, *args, **kwargs)

