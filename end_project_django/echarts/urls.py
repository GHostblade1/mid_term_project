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
from echarts import views
from django.conf.urls import url

app_name = 'echarts'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('bar/', views.f_bar, name='bar'),
    path('broken_line/', views.broken_line, name='broken_line'),
    path('map/', views.f_map, name='map'),
    path('pie/', views.f_pie, name='pie'),
    path('globe/', views.globe, name='globe'),
]
