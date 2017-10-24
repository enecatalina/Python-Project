from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),           #This will be the route to display all the users listings
    url(r'^add$', views.add, name='add'),               #This will be the route to the form in order to sign up a new property
    url(r'^create$', views.create, name='create'),      #This will be the route to create the object in the database
    url(r'^display/(?P<listing_id>\d+)$', views.display, name='display'),   #This will be the route to display a property listing
    url(r'^update/(?P<listing_id>\d+)$', views.update, name='update'),      #This will be the route to update the object in the database
    url(r'^destroy/(?P<listing_id>\d+)$', views.destroy, name='destory'),    #This will be the route to display a property listing
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
