from django.shortcuts import render
from .models import Portfolio

def home(request):
    portfolios = Portfolio.objects.all()
    context = {
        "portfolios": portfolios
    }
    return render(request, "portfolio/home.html", context)


def about(request):
    return render(request, "portfolio/about.html")