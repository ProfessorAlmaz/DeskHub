from django.contrib import admin
from django.urls import path, include

from coworkings import views
from coworkings.views import main_page, register_page

urlpatterns = [
    path('', views.main_page),
    path('register/', register_page, name="register-page"),
    path('main/', main_page, name="main-page"),
]