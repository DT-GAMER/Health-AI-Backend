from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserInteraction
from .serializers import UserInteractionSerializer
from rest_framework.pagination import PageNumberPagination

class UserInteractionHistoryView(APIView):
    """
    API endpoint to retrieve user interaction history.
    """
    permission_classes = [IsAuthenticated]  # Enforce user authentication

    def get(self, request):
        """
        GET request to retrieve user interaction history with pagination and filtering options.
        """
        user_interactions = UserInteraction.objects.filter(user=request.user)  # Fetch interactions for the logged-in user

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 100
        paginated_interactions = paginator.paginate_queryset(user_interactions, request)
        
        serializer = UserInteractionSerializer(paginated_interactions, many=True)
        return paginator.get_paginated_response(serializer.data)

