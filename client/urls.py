from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'client.views.index', name='index'),
]
