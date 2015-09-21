from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Landmark(models.Model):
    name = models.CharField(max_length=30)
    summary_url = models.CharField(max_length=500)
    closest_airport = models.CharField(max_length=3)
    classification_id = models.IntegerField()
    lat = models.DecimalField(decimal_places=5, max_digits=8)
    lon = models.DecimalField(decimal_places=5, max_digits=8)
    image = models.ImageField(upload_to='images', blank=True, null=True)
