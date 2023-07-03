# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:09:47 2023

@author: Imanethepe
"""

from poemscollection import settings
from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import (
    BadHeaderError, send_mail)
from .models import NewsLink, Poem, Tag


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        if new_slug == 'write':
            raise ValidationError(
                'Slug may not be "write".')
        return new_slug


class NewsLinkForm(forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = NewsLink
        ﬁelds = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

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

    def clean_author(self):
        return self.cleaned_data['author'].lower()


class ContactForm(forms.ModelForm):
    """
    Attributes

    name, author and description similar
    to model Poem, plus other attributes.
    """

    class Meta:
        model = Poem
        fields = ['name', 'author', 'description', 'slug']

    email_from = forms.EmailField(initial='')
    reason = forms.CharField(max_length=31)
    recipient_email = forms.EmailField()
    name = forms.CharField(max_length=31)
    author = forms.CharField(max_length=31)
    description = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        reason = self.cleaned_data.get('reason')
        email_from = self.cleaned_data.get('email_from')
        recipient_email = self.cleaned_data.get('recipient_email')
        name = self.cleaned_data.get('name')
        author = self.cleaned_data.get('author')
        description = self.cleaned_data.get('description')
        body = 'Message From: {}\n\n{}-{}\n\n{}\n'.format(
           email_from, name.capitalize(), author.title(), description)
        # print(body)
        try:
            send_mail(
                subject=reason,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient_email.strip()],
                fail_silently=False,
            )
        except BadHeaderError:
            self.add_error(
              None,
              ValidationError(
                'Could Not Send Email.\n'
                'Extra Headers not allowed '
                'in email body.',
                code='badheader'))
            return False
        else:
            return True
