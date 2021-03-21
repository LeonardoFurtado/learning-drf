from django.urls import path

from .views import AuthorAPIView, AuthorsAPIView, BookAPIView, BooksAPIView

urlpatterns = [
    path('authors/<int:pk>', AuthorAPIView.as_view(), name='author'),
    path('authors/', AuthorsAPIView.as_view(), name='authors'),
    path('books/<int:pk>', BookAPIView.as_view(), name='book'),
    path('books/', BooksAPIView.as_view(), name='books'),
]
