from django.urls import path
from .views import create_user, list_all_users, get_user_by_id, add_new_book, list_all_books, get_book_by_id, assign_update_book_details, borrow_book, return_book, list_all_borrowed_books

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('list-all-users/', list_all_users, name='list_all_users'),
    path('get-user-by-id/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('add-new-book/', add_new_book, name='add_new_book'),
    path('list-all-books/', list_all_books, name='list_all_books'),
    path('get-book-by-id/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('assign-update-book-details/<int:book_id>/', assign_update_book_details, name='assign_update_book_details'),
    path('borrow-book/', borrow_book, name='borrow_book'),
    path('return-book/', return_book, name='return_book'),
    path('list-all-borrowed-books/', list_all_borrowed_books, name='list_all_borrowed_books'),
]
