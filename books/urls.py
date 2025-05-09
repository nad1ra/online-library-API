from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    BookCopyListCreateView,
    BookCopyRetrieveUpdateDestroyView,
    AvailableBookCopyListCreateView,
    BookLendingListCreateView,
    BookLendingRetrieveUpdateDestroyView,
    OverdueBookLendingListCreateView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    path('copies/', BookCopyListCreateView.as_view(), name='book-copy-create'),
    path('copies/<int:pk>/', BookCopyRetrieveUpdateDestroyView.as_view(), name='book-copy-detail'),
    path('copies/available/', AvailableBookCopyListCreateView.as_view(), name='available-book-copies'),

    path('lendings/', BookLendingListCreateView.as_view(), name='book-lending-list-create'),
    path('lendings/<int:pk>/', BookLendingRetrieveUpdateDestroyView.as_view(), name='book-lending-detail'),
    path('lendings/overdue/', OverdueBookLendingListCreateView.as_view(), name='overdue-book-lending')
]