from django.db import models
from django.contrib.auth.models import User  # Adjust this based on your User model

class UserInteraction(models.Model):
    """
    Model to store user interactions with the chatbot.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming a ForeignKey relationship with the User model
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    response = models.TextField()

    def __str__(self):
        return f"Interaction by {self.user} at {self.timestamp}"

