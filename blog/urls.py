# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:09:32 2023

@author: Imanethepe
"""

from django.urls import path
from django.urls import re_path
from .views import (
    PostList, PostDetail,
    PostCreate, PostUpdate,
    PostDelete)

urlpatterns = [
    path('',
         PostList.as_view(),
         name='blog_post_list'),
    path(r'create/',
         PostCreate.as_view(),
         name='blog_post_create'),
    re_path(r'(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/$',
            PostDetail.as_view(),
            name='blog_post_detail'),
    re_path(r'(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/'
            r'update/$',
            PostUpdate.as_view(),
            name='blog_post_update'),
    re_path(r'(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/'
            r'delete/$',
            PostDelete.as_view(),
            name='blog_post_delete'),
]
