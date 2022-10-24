from django.contrib import admin
from django.urls import path, include

from .views import home, createshorturl, redirect_url

urlpatterns = [
    path('', home , name= 'home'),
    path('create/', createshorturl, name = 'create'),
    path('<str:url>', redirect_url, name= 'redirect'),
    path('admin/', admin.site.urls),
]
