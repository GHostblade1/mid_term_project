
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register_ok/', views.register_ok, name='register_ok'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('reg_check_name/', views.reg_check_name, name='reg_check_name'),
    path('check_pwd/', views.check_pwd, name='check_pwd'),
    path('get_captcha/', views.get_captcha, name='get_captcha'),
    path('quit/', views.quit, name='quit'),
    path('check_pwd_name/', views.check_pwd_name, name='check_pwd_name'),
    path('user_confirm/', views.user_confirm, name='user_confirm'),
    path('register_ok_re/', views.register_ok_re, name='register_ok_re'),
    path('check_captcha/', views.check_captcha, name='check_captcha'),
]
