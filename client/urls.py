from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'client.views.index', name='index'),
    url(r'^image_search/$', 'client.views.image_search', name='image_search'),
    url(r'^flight_search/$', 'client.views.flight_search', name='flight_search'),
    url(r'^search_result/([0-9]+)/$', 'client.views.search_result', name='search_result'),
]
