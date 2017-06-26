from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.getBusinesses, name='getBusinesses'),
    url(r'^(?P<businessID>[0-9]+)/$',views.businessInfo, name='businessInfo'),
]