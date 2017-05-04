# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib import admin
from news.views import login_action,event_manage,search_name,guest_manage
urlpatterns = [
    url(r'^login_action/',login_action),
    url(r'^event_manage/',event_manage),
    url(r'^search_name/',search_name),
    url(r'^guest_manage/',guest_manage)
   ]