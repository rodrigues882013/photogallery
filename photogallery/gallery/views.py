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

    if request.method == 'GET':
        sorted_method = request.GET['sorted_by']
        images = service.filter_data_set(sorted_method, request.user.is_authenticated)
        return render(request, 'home.html', dict(photos=images, is_authenticated=request.user.is_authenticated))


def photos(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            service.upload_file(request.FILES['image'], request.POST['file_name'])
    else:
        form = ImageForm()

    return render(request, 'photos.html', dict(form=form))


@csrf_exempt
def like(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            return service.like(photo_id=request.POST['photo_id'])

        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(dict(msg="Erro, por favor tente denovo", id_=0)))


@csrf_exempt
def approve(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            return service.approve(photo_id=request.POST['photo_id'])

        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(dict(msg="Erro, por favor tente denovo", id_=0)))
