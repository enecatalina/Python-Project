from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^(?P<listing_id>\d+)/send$', views.send, name="send"),
    url(r'^(?P<listing_id>\d+)/create$', views.create, name="create"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


#   url(r'^(?P<listing_id>\d+)/(?P<message_id>\d+)/create$',
#         views.create, name="create"),
