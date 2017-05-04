# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib import admin
from news.views import login_action,event_manage,search_name,guest_manage,sign_index,sign_index_action
urlpatterns = [
    url(r'^login_action/',login_action),
    url(r'^event_manage/',event_manage),
    url(r'^search_name/',search_name),
    url(r'^guest_manage/',guest_manage),
    url(r'^sign_index/(?P<eid>[0-9]+)/$',sign_index),
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$',sign_index_action),
   ]