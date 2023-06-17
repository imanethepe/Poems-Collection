from django.db import models
from collection.models import Poem, Tag
from django.urls import reverse


class Post(models.Model):
    """Attributes"""
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='A label for URL conﬁg',
        unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToManyField(
        Tag, blank=True, related_name='blog_posts')
    poems = models.ManyToManyField(
       Poem, blank=True, related_name='blog_posts')

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))
