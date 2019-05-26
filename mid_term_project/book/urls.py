
from django.urls import path
from book import views

app_name = 'book'

urlpatterns = [
    path('book_details/', views.book_details, name='book_details'),
    path('booklist/', views.book_list, name='booklist'),
    path('books_order/', views.books_order, name='books_order'),
]