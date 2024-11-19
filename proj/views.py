from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView): #listar
    queryset = Book.objects.all()  # Lista todos os livros da tabela
    serializer_class = BookSerializer  # Usa o BookSerializer criado no serializers.py

class BookCreateView(generics.CreateAPIView): #criar
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
