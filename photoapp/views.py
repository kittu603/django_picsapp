from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Photo

# Create your views here.

def index(request):
    all_photos = Photo.objects.all()
    return render(request,'photoapp/photos.html',{'photos': all_photos})


def detail(request,pk):
    try:
        photo = Photo.objects.get(id=pk)  #getting a particular photo using that id
    except Photo.DoesNotExist:
        raise Http404("Photo not found") #raising an error if someone asks for a photo out of range

    return render(request,'photoapp/detail.html', {'photo': photo})

