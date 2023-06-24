# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:21:53 2023

@author: Imanethepe
"""

from django.shortcuts import render, redirect


class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        print(bound_form.is_bound)
        print(bound_form.is_valid())
        print(bound_form.errors)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})
