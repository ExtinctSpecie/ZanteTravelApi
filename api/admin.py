from django.contrib import admin
from .models import Business, SomeModel, Image

# Register your models here.

admin.site.register(Business)
admin.site.register(Image)
admin.site.register(SomeModel)