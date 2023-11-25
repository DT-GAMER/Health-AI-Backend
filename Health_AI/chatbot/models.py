from django.db import models

class UserInteraction(models.Model):
    """
    Model to store user interactions with the chatbot.
    """

    user = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"User: {self.user.email} - Time: {self.timestamp}"

    class Meta:
        verbose_name = "User Interaction"
        verbose_name_plural = "User Interactions"

