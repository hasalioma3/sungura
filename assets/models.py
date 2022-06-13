from django.db import models


# Create your models here.
class Assets(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
