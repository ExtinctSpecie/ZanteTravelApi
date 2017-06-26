from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BusinessSerializer
from api.models import Business
# Create your views here.


class Businesses(APIView):

    def get(self , request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses , many=True)
        return Response(serializer.data)

    def post(self):
        pass

def getBusinesses(request):
    business = Business.objects.get(pk=1)
    print(business.thumbnail.url)
    return HttpResponse("Hello")

def businessInfo(request , businessID):
    return HttpResponse(str(businessID))