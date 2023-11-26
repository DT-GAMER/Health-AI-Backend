from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"Chat between {self.user.username} at {self.timestamp} - Session: {self.session_id}"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_history = models.ForeignKey('ChatHistory', on_delete=models.CASCADE)
    feedback_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} at {self.timestamp} for Chat ID: {self.chat_history_id}"

