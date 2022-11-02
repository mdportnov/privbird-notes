from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('notes', HomeView.as_view(), name='home'),
    path('notes/<slug:slug>', NoteView.as_view(), name='note'),
    path('support', SupportView.as_view(), name='support'),
]
