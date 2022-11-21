from django.db import models

from feedbacks.utils.Constants import Constants


class Feedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    feedback = models.TextField(max_length=Constants.MAX_FEEDBACK_LENGTH)
    email = models.EmailField(default=None, null=True)

    def __str__(self) -> str:
        author = self.email if self.email else 'anonymous'
        return f'Feedback from {author}'
