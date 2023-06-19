from django.shortcuts import (
    render, get_object_or_404)
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Tag, Poem


class TagList(View):
    """Get request of the list of tags"""

    def get(self, request):
        return render(
                     request,
                     'collection/tag_list.html',
                     {'tag_list': Tag.objects.all()}
                     )


class TagDetail(View):
    """Get request of the detail of a tag"""

    def get(self, request, slug):
        tag = get_object_or_404(
            Tag, slug__iexact=slug)
        return render(
            request,
            'organizer/tag_detail.html',
            {'tag': tag})


class PoemList(View):
    """Get request of the list of pems"""

    def get(self, request):
        return render(
                     request,
                     'collection/poem_list.html',
                     {'poem_list': Poem.objects.all()}
                     )
