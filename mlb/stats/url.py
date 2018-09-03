# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from stats import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^(?P<slug>[\w./-]+)/$', views.page)
    # url(r'^$', TemplateView.as_view(template_name='board/index.html')),

    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^sub/$', views.sub),

    url(r'^post/$', views.post, name='post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^testform/$', views.test_form, name='test_form'),
    url(r'^testDB/$', views.test_db, name='test_db'),
    url(r'^ormSelect/$', views.orm_select, name='orm_select'),
    url(r'^ormFilter/$', views.orm_filter, name='orm_filter'),
]
