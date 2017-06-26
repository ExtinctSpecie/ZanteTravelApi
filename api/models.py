import os

from django.db import models

# Create your models here.

class Business(models.Model):

    position = models.PositiveIntegerField(default=0, unique=False)
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    shortDescription = models.CharField(max_length=128)
    longDescription = models.CharField(max_length=1024)
    phoneNumber = models.CharField(max_length=18)
    email = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    mapCoordinates = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    workingHours = models.CharField(max_length=128)
    price = models.CharField(max_length=64)
    usefulTip = models.CharField(max_length=128)
    creditCards = models.BooleanField(default=False)
    summerOnly = models.BooleanField(default=False)
    thumbnail = models.FileField(upload_to='thumbnails/', default='thumbnails/none/noThumbnail.jpg')

    def __str__(self):
        return self.name + ' - ' + self.location + ' - ' + self.category

class BusinessImages(models.Model):

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='images/', default='images/noImage/noImage.jpg')

    def __str__(self):
        return os.path.basename(self.photo.name)
