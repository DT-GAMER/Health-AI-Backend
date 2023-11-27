from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('chatbot/interaction/', views.chatbot_interaction, name='chatbot_interaction'),
    path('chatbot/feedback/', views.submit_feedback, name='submit_feedback'),
    path('chatbot/rate/', views.rate_chat, name='rate_chat'),
]

