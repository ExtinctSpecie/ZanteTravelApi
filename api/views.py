from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from api.serializers import BusinessSerializer, SomeSerializer, ImageSerializer
from api.models import Business, SomeModel, Image


# Create your views here.

#/businesses/
class Businesses(APIView):

    def get(self , request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#/images/
class Images(APIView):

    def get(self , request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class ImagesOfID(APIView):

    def get(self , request , businessID):
        business = get_object_or_404(Business, pk=businessID)
        try:
            images = business.image_set.all()
            serializer = ImageSerializer(images, many=True)
            return Response(serializer.data)
        except (KeyError,Business.DoesNotExist):
            info = {'success': False, 'info': 'noData'}
            return Response(info)

    def post(self,request):
        pass

class Information(APIView):

    def get(self , request):
        info = {'updateAvailable' : False , 'something' : 'somethingElse'}
        return Response(info)

    def post(self):
        pass

def getBusinesses(request):
    business = Business.objects.get(pk=1)
    print(business.thumbnail.url)
    return HttpResponse("Hello")

def businessInfo(request , businessID):
    return HttpResponse(str(businessID))