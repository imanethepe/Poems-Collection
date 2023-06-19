# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:33:55 2023

@author: Imanethepe
"""

from django.shortcuts import redirect


def redirect_root(request):
    return redirect('collection_poem_list')
