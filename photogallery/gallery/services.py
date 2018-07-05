import boto3
from io import StringIO
from gallery.models import Image


class GalleryService(object):

    @classmethod
    def get_extension(cls, file_name):
        if file_name is not None:
            name_vectors = file_name.split('.')
            ext = name_vectors[len(name_vectors) - 1]
            return ext

    @classmethod
    def upload_file(cls, file, file_name):
        ext = cls.get_extension(file.name)
        client = boto3.client('s3')
        target_bucket = 'images-gallery-app'
        image_path = 'images/' + file_name + '.' + ext

        try:
            client.put_object(Bucket=target_bucket, Key=image_path, Body=file.read())
            cls.save(file, image_path)
        except:
            pass


    @classmethod
    def save(cls, file, image_path):
        pass

    @staticmethod
    def like(form):
        pass

    @staticmethod
    def find(id):
        pass
