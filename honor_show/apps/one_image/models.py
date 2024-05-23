from django.db import models

class image(models.Model):
    name = models.CharField(max_length=30)
    image_path = models.CharField(max_length=20)
    desc = models.TextField()
    where_get = models.IntegerField(default=0)
