from django.shortcuts import render

# Create your views here.
from gallery.models import Image
from gallery.forms import ImageForm
from django.shortcuts import render
from django.template import RequestContext


def home(request):
    return render(request, 'home.html')


def photos(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES['image'])
        if form.is_valid():
            pass

    else:
        form = ImageForm()

    return render(request, 'photos.html', dict(form=form))
