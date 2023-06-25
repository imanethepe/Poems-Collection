# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:04:59 2023

@author: Imanethepe
"""

from django.urls import path
from django.urls import re_path
from .views import (
    TagList, TagDetail, PoemList,
    PoemDetail, TagCreate, PoemWrite,
    NewsLinkCreate, NewsLinkUpdate,
    TagUpdate, PoemUpdate)

urlpatterns = [
    path(r'tag/',
         TagList.as_view(),
         name='collection_tag_list'),
    path(r'tag/create/',
         TagCreate.as_view(),
         name='collection_tag_create'),
    re_path(r'tag/(?P<slug>[\w\-]+)/$',
            TagDetail.as_view(),
            name='collection_tag_detail'),
    re_path(r'tag/(?P<slug>[\w\-]+)/update$',
            TagUpdate.as_view(),
            name='collection_tag_update'),
    path(r'poem/',
         PoemList.as_view(),
         name='collection_poem_list'),
    path(r'poem/write',
         PoemWrite.as_view(),
         name='collection_poem_write'),
    re_path(r'poem/(?P<slug>[\w\-]+)/$',
            PoemDetail.as_view(),
            name='collection_poem_detail'),
    re_path(r'poem/(?P<slug>[\w\-]+)/update$',
            PoemUpdate.as_view(),
            name='collection_poem_update'),
    path(r'newslink/create/',
         NewsLinkCreate.as_view(),
         name='collection_newslink_create'),
    re_path(r'newslink/update/(?P<slug>[\w\-]+)/$',
            NewsLinkUpdate.as_view(),
            name='collection_newslink_update'),
]
