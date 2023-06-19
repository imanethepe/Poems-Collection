# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:09:32 2023

@author: Imanethepe
"""

from django.urls import path
from django.urls import re_path
from .views import PostList, PostDetail

urlpatterns = [
    path('',
         PostList.as_view(),
         name='blog_post_list'),
    re_path(r'(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/$',
            PostDetail.as_view(),
            name='blog_post_detail'),
]
