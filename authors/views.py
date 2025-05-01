from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer
from .paginations import AuthorPagination, AuthorBookPagination
from books.models import Book


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'


class AuthorBookView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorBookPagination

    def get_queryset(self):
        return Book.objects.filter(authors__id=self.kwargs['pk'])