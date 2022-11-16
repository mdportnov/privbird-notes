from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.request import Request

from feedbacks.dto.messages.FeedbackCreated import FeedbackCreatedMessage
from feedbacks.models import Feedback
from feedbacks.dto.serializers.CreateFeedbackSerializer import CreateFeedbackSerializer
from privbird.dto.messages.ApiMessage import ApiMessage


class CreateFeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = CreateFeedbackSerializer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ApiMessage.api_schema()}
    )
    def post(self, request: Request) -> JsonResponse:
        """
        # Send feedback about the service
        """

        self.create(request)
        return FeedbackCreatedMessage().as_json_response()
