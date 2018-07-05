import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from gallery.models import Image
from gallery.forms import ImageForm
from gallery.services import GalleryService as service
from django.shortcuts import render
from django.template import RequestContext

logger = logging.getLogger(__name__)


def home(request):
    return render(request,
                  'home.html',
                  dict(photos=filter(lambda x: x.approved, Image.objects.all())))


def photos(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES['image'])
        if form.is_valid():
            service.upload_file(request.FILES['image'], request.POST['file_name'])

    else:
        form = ImageForm()

    return render(request, 'photos.html', dict(form=form))


@csrf_exempt
def like(request):
    if request.is_ajax():
        try:
            return service.like(likes=request.POST['like'],
                                photo_id=request.POST['photo_id'])

        except ObjectDoesNotExist:
            return HttpResponse(json.dumps(dict(msg="Erro, por favor tente denovo", id_=0)))

