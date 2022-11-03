from django.contrib import admin
from django.urls import path

import feedbacks.views
import notes.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("feedback/", feedbacks.views.PostFeedbackView.as_view()),
    path("notes/", notes.views.PostNoteView.as_view()),
    path("notes/<slug:slug>/", notes.views.NoteView.as_view())
]
