from django.shortcuts import (
    render, get_object_or_404)
from django.views.generic import View
from .models import Post


class PostList(View):
    """get request of the list"""

    def get(self, request):
        """List of posts"""
        return render(
            request,
            'blog/post_list.html',
            {'post_list': Post.objects.all()})


class PostDetail(View):
    """get request of the detail of a post"""

    def get(self, request, year, month, slug):
        """Detail of a post"""
        post = get_object_or_404(
         Post,
         pub_date__year=year,
         pub_date__month=month,
         slug=slug)
        return render(
            request,
            'blog/post_detail.html',
            {'post': post})
