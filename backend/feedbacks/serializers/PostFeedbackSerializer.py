from rest_framework import serializers

from feedbacks.models import Feedback


class PostFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback', 'email']
