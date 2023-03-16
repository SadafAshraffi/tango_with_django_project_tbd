from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views


app_name='rango'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
# path('category/<slug:category_name_slug>/add_page/',views.add_page, name='add_page'),

path('admin/', admin.site.urls),
]



