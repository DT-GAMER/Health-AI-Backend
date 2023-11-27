from rest_framework import serializers
from .models import ChatHistory, Feedback

class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'message', 'response', 'timestamp', 'session_id', 'rating']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'chat_history', 'feedback_text', 'timestamp']

