from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    
    path('', views.books_list, name='books-list'),
    path('books_add/', views.books_add, name='books-add'),
    path('books_add/book_added/', views.book_added, name='books-added'),
    path('books_detail/<int:book_id>', views.books_detail, name='books-deatil'),
    path('books_delete/<int:book_id>', views.books_delete, name='books-delete'),
    path('books_update/<int:book_id>', views.books_update, name='books-update')
]