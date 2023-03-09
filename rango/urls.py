from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views


app_name='rango'

urlpatterns = [
path('', views.index, name='index'),
path('about', views.index, name='about'),
path('admin/', admin.site.urls),
]
