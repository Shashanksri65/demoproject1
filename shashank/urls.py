from django.conf.urls import include, url
from . import views


app_name = 'shashank'


urlpatterns = [

    # /shashank/
    url(r'^$', views.IndexView.as_view(), name='index'),


    # /shashank/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
