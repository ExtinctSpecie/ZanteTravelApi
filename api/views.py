from django.http import HttpResponse
from django.shortcuts import render
from .models import Business
# Create your views here.

def getBusinesses(request):
    business = Business.objects.get(pk=1)
    print(business.thumbnail.url)
    return HttpResponse("Hello")

def businessInfo(request , businessID):
    return HttpResponse(str(businessID))