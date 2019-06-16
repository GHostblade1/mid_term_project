from django.urls import path
from commodity import views

app_name = 'commodity'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('dzlist/', views.dzlist, name='dzlist'),
    path('list/', views.list, name='list'),
    path('splb/', views.splb, name='splb'),
    path('test/', views.test, name='test'),
    path('zjsp/', views.zjsp, name='zjsp'),
    path('zjzlb/', views.zjzlb, name='zjzlb'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_p_c/', views.add_p_c, name='add_p_c'),
    path('add_c_c/', views.add_c_c, name='add_c_c'),
    path('delete_books/', views.delete_books, name='delete_books')

]