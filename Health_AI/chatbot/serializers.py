from rest_framework import serializers
from .models import UserInteraction

class UserInteractionSerializer(serializers.ModelSerializer):
    """
    Serializer for UserInteraction model.
    """

    class Meta:
        model = UserInteraction
        fields = ['id', 'user', 'timestamp', 'message', 'response']
        read_only_fields = ['id', 'user', 'timestamp', 'response']

