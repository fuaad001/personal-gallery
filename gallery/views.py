from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Location, Category, Photographer

# Create your views here.
def index(request):
    images = Image.objects.all()

    return render(request, 'index.html', {"images": images})
