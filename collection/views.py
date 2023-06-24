from django.shortcuts import (
    render, get_object_or_404)
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Tag, Poem
from .forms import (
    TagForm, PoemForm,
    NewsLinkForm)
from .utils import ObjectCreateMixin

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
            'collection/tag_detail.html',
            {'tag': tag})


class PoemList(View):
    """Get request of the list of pems"""

    def get(self, request):
        return render(
                     request,
                     'collection/poem_list.html',
                     {'poem_list': Poem.objects.all()}
                     )


class PoemDetail(View):
    """Get request of the detail of a poem"""

    def get(self, request, slug):
        poem = get_object_or_404(
            Tag, slug__iexact=slug)
        return render(
            request,
            'collection/poem_detail.html',
            {'poem': poem})


class TagCreate(ObjectCreateMixin, View):
    """Post request of a new tag"""

    form_class = TagForm
    template_name = 'collection/tag_form.html'


class PoemWrite(ObjectCreateMixin, View):
    """Post request of a new poem"""

    form_class = PoemForm
    template_name = 'collection/poem_form.html'


class NewsLinCreate(ObjectCreateMixin, View):
    """Post new link to article"""

    form_class = NewsLinkForm
    template_name = 'collection/newslink_form.html'
