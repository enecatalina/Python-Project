from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^login$', views.login, name="login"),
    url(r'^success$', views.success_login, name="success"),
    url(r'^logout$', views.logout, name="logout"),

]
