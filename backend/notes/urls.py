from django.urls import path

from notes import views

urlpatterns = [
    path('', views.CreateNoteView.as_view()),
    path('<slug:slug>-<key>/', views.NoteView.as_view()),
    path('<slug:slug>/', views.NoteView.as_view())
]
