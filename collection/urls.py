# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:04:59 2023

@author: Imanethepe
"""

from django.urls import path
from django.urls import re_path
from .views import (
    TagList, TagDetail, PoemList,
    )

urlpatterns = [
    path(r'tag/',
         TagList.as_view(),
         name='collection_tag_list'),
    re_path(r'tag/(?P<slug>[\w\-]+)/$',
            TagDetail.as_view(),
            name='collection_tag_detail'),
    path(r'poem/',
         PoemList.as_view(),
         name='collection_poem_list'),
]
