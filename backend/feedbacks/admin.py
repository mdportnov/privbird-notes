from django.contrib import admin

from feedbacks.models import Feedback
from feedbacks.utils.constants import Constants


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'email', 'feedback_preview')
    list_filter = ('created_at',)
    search_fields = ('email', 'feedback')

    @admin.display(description='feedback')
    def feedback_preview(self, model: Feedback):
        preview = model.feedback
        if len(preview) > Constants.FEEDBACK_PREVIEW_LENGTH:
            preview = preview[:Constants.FEEDBACK_PREVIEW_LENGTH] + '...'
        return preview
