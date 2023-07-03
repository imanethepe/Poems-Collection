from django.shortcuts import (
    render, get_object_or_404, redirect)
from django.contrib.messages import success
from django.views.generic import View
from django.urls import reverse_lazy
from .models import (
    Tag, Poem, NewsLink)
from .forms import (
    TagForm, PoemForm,
    NewsLinkForm, ContactForm)
from .utils import (
    ObjectCreateMixin, ObjectUpdateMixin,
    ObjectDeleteMixin,)

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
            Poem, slug__iexact=slug)
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


class NewsLinkCreate(ObjectCreateMixin, View):
    """Post new link to article"""

    form_class = NewsLinkForm
    template_name = 'collection/newslink_form.html'


class NewsLinkUpdate(View):
    """Update link to article"""

    form_class = NewsLinkForm
    model = NewsLink
    template_name = (
        'collection/newslink_form_update.html')

    def get(self, request, slug):
        newslink = get_object_or_404(
             self.model, slug=slug)
        context = {
             'form': self.form_class(
                 instance=newslink),
             'newslink': newslink,
        }
        return render(
             request, self.template_name, context)

    def post(self, request, slug):
        newslink = get_object_or_404(
             self.model, slug=slug)
        bound_form = self.form_class(
             request.POST, instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                 'form': bound_form,
                 'newslink': newslink,
            }
            return render(
                 request,
                 self.template_name,
                 context)


class TagUpdate(ObjectUpdateMixin, View):
    """Update a tag"""

    form_class = TagForm
    model = Tag
    template_name = (
       'collection/tag_form_update.html')


class PoemUpdate(ObjectUpdateMixin, View):
    """Update a poem"""

    form_class = PoemForm
    model = Poem
    template_name = (
       'collection/poem_form_update.html')


class NewsLinkDelete(View):
    """Delete link to article"""

    def get(self, request, slug):
        newslink = get_object_or_404(
            NewsLink, slug=slug)
        return render(
            request,
            'collection/'
            'newslink_form_delete.html',
            {'newslink': newslink})

    def post(self, request, slug):
        newslink = get_object_or_404(
            NewsLink, slug=slug)
        poem = newslink.poem
        newslink.delete()
        return redirect(poem)


class TagDelete(ObjectDeleteMixin, View):
    """Delete a tag"""

    model = Tag
    success_url = reverse_lazy(
        'collection_tag_list')
    template_name = (
       'collection/tag_form_delete.html')


class PoemDelete(ObjectDeleteMixin, View):
    """Delete a poem"""

    model = Poem
    success_url = reverse_lazy(
        'collection_poem_list')
    template_name = (
       'collection/poem_form_delete.html')


class ContactView(View):
    form_class = ContactForm
    template_name = 'collection/contact_form.html'

    # def get(self, request):
    # return render(request,
    #               self.template_name,
    #               {'form': self.form_class()})
    def get(self, request, slug):
        obj = get_object_or_404(
            Poem, slug=slug)
        context = {
            'form': self.form_class(instance=obj),
            'poem': obj,
        }
        return render(request,
                      self.template_name,
                      context)

    def post(self, request, slug):
        obj = get_object_or_404(
            Poem, slug__iexact=slug)
        bound_form = self.form_class(
            request.POST, instance=obj)
        # print(bound_form.errors)
        if bound_form.is_valid():
            mail_sent = bound_form.send_mail()
            if mail_sent:
                # shortcut for add_message
                success(
                  request,
                  'Email successfully sent.')
                return redirect('collection_poem_list')
        return render(request,
                      self.template_name,
                      {'form': bound_form})
