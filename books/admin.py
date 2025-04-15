from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('authors', 'title', 'desc')
    search_fields = ('authors', 'title', 'desc', 'genre', 'page_count')