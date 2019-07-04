"""end_project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('register/', views.register_logic, name='register'),
    path('re_check_name/', views.re_check_name, name='re_check_name'),
    path('re_check_phone/', views.re_check_phone, name='re_check_phone'),
    path('re_check_pwd/', views.re_check_pwd, name='re_check_pwd'),
]
