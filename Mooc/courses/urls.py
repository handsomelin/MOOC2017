# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib.auth.views import password_change_done
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^$', home, name='home', ),
    url(r'^addcourses/$', addcourses, name='addcourses', ),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^deleteCourses/(?P<pk>\d+)/$', deleteCourses, name='deleteCourses', ),
    url(r'^keywords/(?P<pk>\d+)/$',keywords, name='keywords',),
    url(r'^deletekeywords/(?P<pk>\d+)/$',deletekeywords, name='deletekeywords', ),
    url(r'^addkeywords/(?P<pk>\d+)$',addkeywords, name='addkeywords', )
]
