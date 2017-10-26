from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^signup$', views.index, name="index"),        #This route takes us to the registration page
    url(r'^logme$', views.logme, name="logme"),         # This route takes us to the login form
    url(r'^create$', views.create, name="create"),          #This route processes the registration form
    url(r'^login$', views.login, name="login"),             #This route processes the login form
    url(r'^(?P<user_id>\d+)/edit$', views.edit, name="edit"),       #This route renders the edit form
    url(r'^(?P<user_id>\d+)/update$', views.update, name="update"),     #THis route processes the edit form
    url(r'^(?P<user_id>\d+)/view$', views.view, name="view"),           #this route displays the users profile
    url(r'^logout$', views.logout, name="logout"),                      #This route logs the user out (using that session) and returns us to the registration page

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
