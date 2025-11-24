from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from coworkings.forms import CustomUserCreationForm


def main_page(request: HttpRequest):
    return render(request, 'index.html')


def auth_page(request: HttpRequest):
    form = UserCreationForm()
    return render(
        request,
        "auth.html",
        context={"form": form}
    )

def registration_page(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "profile.html", context={"user": user})
        else:
            return render(
                request,
                "registration.html",
                context={"form": form, "errors": form.errors}
            )
    else:
        form = CustomUserCreationForm()
        return render(
            request,
            "registration.html",
            context={"form": form, "errors": {}}
        )

def profile_page(request: HttpRequest):
    form = UserCreationForm()
    return render(
        request,
        "profile.html",
        context={"form": form}
    )