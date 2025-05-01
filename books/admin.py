from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'authors_display', 'title', 'desc')
    search_fields = ('authors', 'title', 'desc', 'genre', 'page_count')

    def authors_display(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    authors_display.short_description = 'Authors'


class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'inventory_number', 'condition')
    search_fields = ('book', 'inventory_number')


class BookLendingAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_copy', 'borrower_name', 'borrower_email', 'borrowed_date')
    search_fields = ('book_copy', 'borrower_name', 'borrower_email')