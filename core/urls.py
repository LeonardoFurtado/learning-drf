from django.urls import path

from .views import AuthorAPIView, BookAPIView

urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('books/', BookAPIView.as_view(), name='books'),
]
