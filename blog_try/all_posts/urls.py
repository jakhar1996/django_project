from django.conf.urls import url
from django.contrib import admin
from all_posts.views import (post_create, post_detail, post_update, post_list, post_delete)


urlpatterns = [
    url(r'^$', post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', post_create, name="post_create"),
    url(r'^detail/$', post_detail, name="post_detail"),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name="post_delete"),
]
