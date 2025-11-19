from django.contrib import admin
from django.urls import path, include

from coworkings import views
from coworkings.views import main_page, auth_page, registration_page, profile_page

urlpatterns = [
    path('', views.main_page),
    path('main/', main_page, name="main-page"),
    path('auth/', auth_page, name="auth-page"),
    path('registration/', registration_page, name="registration-page"),
    path('profile/', profile_page, name="profile-page"),
]