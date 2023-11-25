from django.urls import path
from .views import UserInteractionHistoryView

urlpatterns = [
    path('interaction-history/', UserInteractionHistoryView.as_view(), name='interaction-history'),
]

