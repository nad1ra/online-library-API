from rest_framework import generics
from .models import Book, BookLending, BookCopy
from .serializers import BookSerializer, BookLendingSerializer, BookCopySerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer


class BookCopyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    lookup_field = 'pk'


class AvailableBookCopyListCreateView(generics.ListAPIView):
    serializer_class = BookCopySerializer

    def get_queryset(self):
        return BookCopy.objects.filter(is_available=True)


class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer
    lookup_field = 'pk'


class BookLendingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer
    lookup_field = 'pk'

class OverdueBookLendingListCreateView(generics.ListAPIView):
    serializer_class = BookLendingSerializer

    def get_queryset(self):
        return BookLending.objects.filter(status='overdue')