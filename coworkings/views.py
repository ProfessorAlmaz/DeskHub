from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def main_page(request: HttpRequest):
    return render(request, 'index.html')


def registration_page(request: HttpRequest):
    form = UserCreationForm()
    return render(
        request,
        "registration.html",
        context={"form": form}
    )