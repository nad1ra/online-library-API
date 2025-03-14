from rest_framework import serializers
from .models import Book, BookCopy, BookLending


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'desc', 'page_count', 'language']


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ['id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date']


class BookLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = ['id', 'book_copy', 'borrower_name', 'borrower_email', 'borrowed_date', 'due_date', 'returned_date', 'status']


