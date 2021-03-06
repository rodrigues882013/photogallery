import json
import logging
import boto3
from django.http import HttpResponse
from gallery.models import Image
from django.conf import settings

logger = logging.getLogger(__name__)


class GalleryService(object):

    @classmethod
    def get_extension(cls, file_name):
        if file_name is not None:
            name_vectors = file_name.split('.')
            ext = name_vectors[len(name_vectors) - 1]
            return ext

    @classmethod
    def upload_file(cls, file, file_name):
        if Image.objects.all().count() > 500:
            logger.error('Operation is not allowed.')
            raise Exception('Operation is not allowed')

        logger.info("Uploading image")
        ext = cls.get_extension(file.name)
        client = boto3.client('s3')
        target_bucket = settings.S3_BUCKET
        image_path = 'images/' + file_name + '.' + ext

        try:
            client.put_object(Bucket=target_bucket, Key=image_path, Body=file.read())
            cls.save(file_name, 'https://s3.amazonaws.com/' + target_bucket + '/' + image_path)
        except Exception as ex:
            logger.error(ex)

    @classmethod
    def save(cls, file_name, image_path):
        logger.info("Save images")
        image = Image(url=image_path, approved=False, file_name=file_name)
        image.save()

    @staticmethod
    def like(**kwargs):
        if not kwargs.get("photo_id"):
            return HttpResponse(json.dumps(dict(msg="Something wrong, try again.")))

        image = Image.objects.get(id=kwargs.get("photo_id"))
        Image.objects.filter(id=kwargs.get("photo_id")).update(likes=image.likes + 1)
        return HttpResponse(json.dumps(dict(message="Liked with success", liked=image.likes + 1)))

    @staticmethod
    def approve(**kwargs):
        if not kwargs.get("photo_id"):
            return HttpResponse(json.dumps(dict(message="Something wrong, try again.")))

        Image.objects.filter(id=kwargs.get("photo_id")).update(approved=True)
        return HttpResponse(json.dumps(dict(message="Photo approved with success.")))

    @staticmethod
    def filter_data_set(sorted_method, is_authenticated):
        logger.debug("Filtering data")

        if is_authenticated:
            if sorted_method not in ['upload_date', 'likes']:
                photos = Image.objects.all()
            else:
                photos = Image.objects.order_by('-' + sorted_method)
        else:
            if sorted_method not in ['upload_date', 'likes']:
                photos = Image.objects.filter(approved=True)
            else:
                photos = Image.objects.order_by('-' + sorted_method).filter(approved=True)

        return photos
