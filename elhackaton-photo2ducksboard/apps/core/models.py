import json
import requests
from requests.auth import HTTPBasicAuth

from django.db import models
from django.conf import settings


class PhotoManager(models.Manager):
    def get_all_photos(self):
        return self.all().order_by('-id')


class Photo(models.Model):
    def image_path(instance, filename):
        return 'photos/' + filename

    image = models.ImageField(upload_to=image_path)
    date = models.DateTimeField(auto_now_add=True)

    objects = PhotoManager()

    def send_to_ducksboard(self):
        data = json.dumps({'value': {'source': self.image.url}})
        auth = HTTPBasicAuth(settings.DUCKSBOARD_APIKEY, 'x')
        requests.post(settings.DUCKSBOARD_WIDGET_URL, auth=auth, data=data)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        self.send_to_ducksboard()

