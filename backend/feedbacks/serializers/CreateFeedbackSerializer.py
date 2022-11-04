from rest_framework import serializers

from feedbacks.models import Feedback


class CreateFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback', 'email']
