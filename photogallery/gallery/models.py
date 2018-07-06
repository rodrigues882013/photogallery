

from django.db import models


# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    file_name = models.CharField(max_length=120)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.file_name
