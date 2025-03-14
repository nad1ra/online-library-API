from django.db import models
from authors.models import Author
from genres.models import Genre


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')
    isbn = models.CharField(max_length=15, unique=True)
    published_date = models.DateField()
    desc = models.TextField()
    page_count = models.IntegerField()
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BookCopy(models.Model):
    CONDITION_TYPES = [
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='books')
    inventory_number = models.CharField(max_length=15, unique=True)
    condition = models.CharField(max_length=10, choices=CONDITION_TYPES, default='new')
    is_available = models.BooleanField()
    added_date = models.DateTimeField()

    def __str__(self):
        return self.book.title if self.book else "No book"


class BookLending(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]
    book_copy = models.ForeignKey(BookCopy, on_delete=models.SET_NULL, null=True, related_name='books')
    borrower_name = models.CharField(max_length=100)
    borrower_email = models.EmailField()
    borrowed_date = models.DateTimeField()
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.borrower_name} - {self.book_copy.book.title if self.book_copy.book else 'No book'}"