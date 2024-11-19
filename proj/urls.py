from django.urls import path
from .views import BookListView, BookCreateView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('add/', BookCreateView.as_view()),
]