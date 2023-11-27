
from .bot import get_openai_response
from django.http import JsonResponse, HttpResponseBadRequest
from .models import ChatHistory, Feedback
from .serializers import ChatHistorySerializer, FeedbackSerializer

def chatbot_interaction(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        session_id = request.POST.get('session_id')

        if not user_input:
            return HttpResponseBadRequest('Message parameter is missing or empty.')

        try:
            # Get AI/ML response using the model function
            response = get_openai_response(user_input)

            # Save chat history in the database
            chat_history = ChatHistory.objects.create(user=request.user, message=user_input,
                                                      response=response, session_id=session_id)

            # Return JSON response with chatbot output
            return JsonResponse({'response': response})
        except Exception as e:
            # Handle exceptions - log the error, return an appropriate response
            return JsonResponse({'error': 'An error occurred while processing your request.'}, status=500)

def submit_feedback(request):
    if request.method == 'POST':
        user_feedback = request.POST.get('feedback')
        chat_history_id = request.POST.get('chat_history_id')

        if not user_feedback or not chat_history_id:
            return HttpResponseBadRequest('Feedback or chat history ID missing.')

        try:
            chat_history = ChatHistory.objects.get(pk=chat_history_id)
            feedback = Feedback.objects.create(user=request.user, chat_history=chat_history,
                                               feedback_text=user_feedback)

            return JsonResponse({'message': 'Feedback submitted successfully.'})
        except ChatHistory.DoesNotExist:
            return HttpResponseBadRequest('Invalid chat history ID.')
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while processing your request.'}, status=500)

def rate_chat(request):
    if request.method == 'POST':
        chat_history_id = request.POST.get('chat_history_id')
        rating = request.POST.get('rating')

        if not chat_history_id:
            return HttpResponseBadRequest('Chat history ID missing.')

        try:
            chat_history = ChatHistory.objects.get(pk=chat_history_id)
            if rating:
                chat_history.rating = rating
                chat_history.save()

            return JsonResponse({'message': 'Chat rated successfully.'})
        except ChatHistory.DoesNotExist:
            return HttpResponseBadRequest('Invalid chat history ID.')
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while processing your request.'}, status=500)

