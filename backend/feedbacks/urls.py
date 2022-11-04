from django.urls import path

from feedbacks import views

urlpatterns = [
    path('', views.PostFeedbackView.as_view())
]
