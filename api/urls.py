from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^businesses/$',views.Businesses.as_view(), name='businesses'),
    url(r'^businesses/(?P<businessGroupID>[0-9]+)/$',views.GroupBusinesses.as_view(), name='business'),
    url(r'^images/$',views.Images.as_view(), name='images'),
    url(r'^images/(?P<businessID>[0-9]+)/$',views.ImagesOfID.as_view(), name='business'),
    url(r'^information/$',views.Information.as_view(), name='information'),
]