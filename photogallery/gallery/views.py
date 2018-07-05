import json
import logging

from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from gallery.models import Image
from gallery.forms import ImageForm
from gallery.services import GalleryService as service
from django.shortcuts import render, redirect
from django.template import RequestContext

logger = logging.getLogger(__name__)


def home(request):
    if request.user.is_authenticated:
        images = Image.objects.all()
    else:
        images = filter(lambda x: x.approved, Image.objects.all())

    return render(request, 'home.html', dict(photos=images, is_authenticated=request.user.is_authenticated))


def photos(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES['image'])
        if form.is_valid():
            service.upload_file(request.FILES['image'], request.POST['file_name'])

    else:
        form = ImageForm()

    return render(request, 'photos.html', dict(form=form))


def do_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Redirect to a success page.
        redirect(to='home')
    else:
        # Return an 'invalid login' error message.
        redirect(to='error')


@csrf_exempt
def like(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            return service.like(likes=request.POST['like'],
                                photo_id=request.POST['photo_id'])

        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(dict(msg="Erro, por favor tente denovo", id_=0)))


@csrf_exempt
def approve(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            return service.approve(photo_id=request.POST['photo_id'])

        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(dict(msg="Erro, por favor tente denovo", id_=0)))
