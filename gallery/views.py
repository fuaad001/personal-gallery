from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Location, Category, Photographer

# Create your views here.
def index(request):
    images = Image.objects.all()

    return render(request, 'index.html', {"images": images})

def search_page(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# def sortby_locations(request):
#     images = Image.filter_by_location()
#
#     return render(request, 'location.html', {"images":images})
#
# def single_image(request, image_id):
#     image = Image.get_image_by_id(image_id)
#     return render(request, 'single_image.html', {"image":image})
