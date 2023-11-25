from rest_framework import serializers
from .models import UserInteraction

class UserInteractionSerializer(serializers.ModelSerializer):
    """
    Serializer for UserInteraction model.
    """

    class Meta:
        model = UserInteraction
        fields = ['id', 'timestamp', 'message', 'response']
        read_only_fields = ['id', 'timestamp', 'message', 'response']

