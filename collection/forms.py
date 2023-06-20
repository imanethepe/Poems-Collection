# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:09:47 2023

@author: Imanethepe
"""

from django import forms
from django.core.exceptions import ValidationError
from .models import NewsLink, Poem, Tag


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug


class NewsLinkForm(
        SlugCleanMixin, forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = NewsLink
        ﬁelds = '__all__'


class TagForm(
        SlugCleanMixin, forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = Tag
        ﬁelds = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class PoemForm(
        SlugCleanMixin, forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = Poem
        ﬁelds = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()
