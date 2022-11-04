from django.urls import path

from notes import views

urlpatterns = [
    path('', views.PostNoteView.as_view()),
    path('<slug:slug>/', views.NoteView.as_view())
]
