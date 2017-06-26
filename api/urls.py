from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Businesses.as_view(), name='getBusinesses'),
    url(r'^(?P<businessID>[0-9]+)/$',views.Businesses.as_view(), name='businessInfo'),
]