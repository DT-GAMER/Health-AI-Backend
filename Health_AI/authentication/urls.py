from django.urls import path
from .views import RegisterUserView, LoginUserView, GoogleLoginView, LogoutView

urlpatterns = [
    path('/account/register', RegisterUserView.as_view(), name='register'),
    path('/account/login', LoginUserView.as_view(), name='login'),
    path('/account/logout', LogoutView.as_view(), name='logout'),
    path('/account/google', GoogleLoginView.as_view(), name='google_login'),
]

