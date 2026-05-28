from django.contrib import admin
from django.urls import path
from converter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('convert/', views.convert, name='convert'),
]
