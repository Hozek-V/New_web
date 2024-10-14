from django.shortcuts import render
from django.template import loader

# Create your views here.

def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")