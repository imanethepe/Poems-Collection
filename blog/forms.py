# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:14:58 2023

@author: Imanethepe
"""

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        ﬁelds = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
