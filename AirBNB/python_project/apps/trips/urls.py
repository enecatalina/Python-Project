from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.booking, name = 'bookinghome'),
    url(r'^show/(?P<listing_id>\d+)$', views.showlocation, name = 'showlocation'),
    url(r'^bookatrip/(?P<listing_id>\d+)$', views.bookatrip, name = 'booktrip'),
    url(r'^mytrips/$', views.mytrips, name = 'mytrips'),
    # url(r'^create$', views.create, name="create"),
    # url(r'^login$', views.login, name="login"),
    # url(r'^success$', views.success_login, name="success"),
    # url(r'^logout$', views.logout, name="logout"),

] 
    