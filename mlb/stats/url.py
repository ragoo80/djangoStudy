# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
# from stats import views


urlpatterns = [
    # url(r'^(?P<slug>[\w./-]+)/$', views.page)

    # url(r'^index/$', views.index, name="index"),
    # url(r'^team(?P<team_name>[\w./-]+)/$', views.team, name='team'),
    # url(r'^player(?P<player_id>[\w./-]+)/$', views.player, name='player'),


    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^sub/$', views.sub),
]

