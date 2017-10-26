from django.conf.urls import include, url
from . import views


app_name = 'shashank'


urlpatterns = [

    # /shashank/
    url(r'^$', views.index, name='index'),


    # /shashank/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),


    # /shashank/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
