from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import LoginForm

# Create your views here.
def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("portfolio")
        messages.error(request, "invalid user or password")
        return render(request, "users/login.html", {"form": form})