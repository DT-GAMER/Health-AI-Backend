from django.urls import path
from .views import UserInteractionView

urlpatterns = [
    path('interaction/', UserInteractionView.as_view(), name='user-interaction'),
]

