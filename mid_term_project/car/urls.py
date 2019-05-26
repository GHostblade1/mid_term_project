from django.urls import path
from car import views

app_name = 'car'

urlpatterns = [
    path('car_f/', views.car, name='car_f'),
    path('indent/', views.indent, name='indent'),
    path('indent_ok/', views.indent_ok, name='indent_ok'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('delete_book_inCart/', views.delete_book_inCart, name='delete_book_inCart'),
    path('red_amount/',  views.red_amount, name='red_amount'),
    path('add_amount/', views.add_amount, name='add_amount'),
    path('recover_book_inCart/', views.recover_book_inCart, name='recover_book_inCart'),
]