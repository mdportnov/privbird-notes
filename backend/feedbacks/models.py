from django.db import models


class Feedback(models.Model):
    feedback = models.TextField()
    email = models.EmailField(default=None, null=True)
