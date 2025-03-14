from rest_framework import serializers
from .models import Book, BookCopy, BookLending


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = '__all__'


class BookLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = '__all__'


