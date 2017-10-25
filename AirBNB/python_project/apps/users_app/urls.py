from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup$', views.index, name="index"),
    url(r'^logme$', views.logme, name="logme"),
    url(r'^home$', views.newhome, name="newhome"),
    url(r'^create$', views.create, name="create"),
    url(r'^login$', views.login, name="login"),
    # url(r'^success$', views.success_login, name="success"),
    url(r'^(?P<user_id>\d+)/edit$', views.edit, name="edit"),
    url(r'^(?P<user_id>\d+)/update$', views.update, name="update"),
    url(r'^(?P<user_id>\d+)/view$', views.view, name="view"),
    # url(r'^(?P<friend_id>\d+)/destroy$', views.destroy, name="destroy"),
    url(r'^logout$', views.logout, name="logout"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
