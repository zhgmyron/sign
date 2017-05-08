# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib import admin
from news import views_if
urlpatterns = [
    url(r'^user_sign/',views_if.user_sign,name='user_sign'),
    url(r'^add_event/',views_if.add_event,name='add_event'),
    url(r'^add_guest/',views_if.add_guest,name='add_guest'),
    url(r'^get_event_list/',views_if.get_event_list,name='get_event_list'),
    url(r'^get_guest_list/',views_if.get_guest_list,name='get_guest_list'),
    # # url(r'^guest_manage/',guest_manage),
    # # url(r'^sign_index/(?P<eid>[0-9]+)/$',sign_index),
    # # url(r'^sign_index_action/(?P<eid>[0-9]+)/$',sign_index_action),
   ]