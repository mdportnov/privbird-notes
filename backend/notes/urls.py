from django.urls import path

from notes import views

urlpatterns = [
    path('', views.CreateNoteView.as_view()),
    path('<slug:slug>/', views.NotePasswordView.as_view()),
    path('<slug:slug>/<slug:key>/', views.NoteKeyView.as_view())
]
