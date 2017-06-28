from rest_framework import serializers
from .models import Business, SomeModel, Image


class BusinessSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(max_length=None,use_url=True)

    class Meta:
        model = Business
        #fields = ('position','name')
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = '__all__'

class SomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = '__all__'