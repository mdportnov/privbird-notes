from django.db import models

from feedbacks.utils.constants import Constants


class Feedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    feedback = models.TextField(max_length=Constants.MAX_FEEDBACK_LENGTH)
    email = models.EmailField(default=None, null=True)
