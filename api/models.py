import os

import datetime
from django.db import models

# Create your models here.

# GroupID AND Group !!
# menuItems.put(0, R.id.aboutZante);
# menuItems.put(1, R.id.attractions);
# menuItems.put(2, R.id.accommodation);
# menuItems.put(3, R.id.food);
# menuItems.put(4, R.id.entertainment);
# menuItems.put(5, R.id.shopping);
# menuItems.put(6, R.id.activities);
# menuItems.put(7, R.id.beaches);
# menuItems.put(8, R.id.rentals);
# menuItems.put(9, R.id.other);
# menuItems.put(10, R.id.emergencyHelp);

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
    group = models.CharField(max_length=128)
    groupID = models.PositiveIntegerField(default=-1)
    category = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    workingHours = models.CharField(max_length=128)
    price = models.CharField(max_length=64, blank=True)
    usefulTip = models.CharField(max_length=128, blank=True)
    isPremium = models.BooleanField(default=False)
    creditCards = models.BooleanField(default=False)
    summerOnly = models.BooleanField(default=False)
    isRecommended = models.BooleanField(default=False)
    thumbnailURL = models.TextField(max_length=1024)
    thumbnail = models.FileField(upload_to='thumbnails/', default='thumbnails/none/noThumbnail.jpg')
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name + ' - ' + self.location + ' - ' + self.category

class Image(models.Model):
    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0, unique=False)
    imageURL = models.TextField(max_length=1024)
    image = models.FileField(upload_to='images/', default='images/none/noThumbnail.jpg')

    def __str__(self):
        return self.business.name + ' - ' + str(self.position) + ' - ' + self.imageURL

class SomeModel(models.Model):
    position = models.PositiveIntegerField(default=0, unique=False)
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    image = models.FileField(upload_to='images/', default='images/none/noThumbnail.jpg')
    def __str__(self):
        return self.name + ' - ' + self.location