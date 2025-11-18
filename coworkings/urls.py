from django.contrib import admin
from django.urls import path, include

from coworkings import views
from coworkings.views import main_page, registration_page

urlpatterns = [
    path('', views.main_page),
    path('registration/', registration_page, name="registration-page"),
    path('main/', main_page, name="main-page"),
]