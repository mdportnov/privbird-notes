from rest_framework import generics, mixins, status
from rest_framework.request import Request
from rest_framework.response import Response

from feedbacks.messages.FeedbackCreated import FeedbackCreatedMessage
from feedbacks.models import Feedback
from feedbacks.serializers.PostFeedbackSerializer import PostFeedbackSerializer


class PostFeedbackView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Feedback.objects.all()
    serializer_class = PostFeedbackSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        self.create(request, args, kwargs)
        message = FeedbackCreatedMessage().serialize()
        return Response(message, status=status.HTTP_201_CREATED)
