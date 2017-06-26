from rest_framework import serializers
from .models import Business


class BusinessSerializer(serializers.ModelSerializer):

    #thumbnail = serializers.SerializerMethodField('getThumbnailURL')
    #can use the below as well
    
    thumbnail = serializers.ImageField(max_length=None,use_url=True)



    class Meta:
        model = Business
        #fields = ('position','name')
        fields = '__all__'

    def getThumbnailURL(self, obj):
        #relative path
        return obj.thumbnail.url