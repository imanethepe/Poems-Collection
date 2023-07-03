from django.db import models
from django.urls import reverse


class Tag(models.Model):
    """Attributes"""

    name = models.CharField(
        max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL conﬁg.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection_tag_detail',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('collection_tag_update',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('collection_tag_delete',
                       kwargs={'slug': self.slug})


class Poem(models.Model):
    """Attributes"""

    name = models.CharField(
        max_length=31, db_index=True)
    author = models.CharField(
        max_length=31, db_index=True)
    slug = models.SlugField(
         max_length=31,
         unique=True,
         help_text='A label for URL conﬁg.')
    description = models.TextField()
    founded_date = models.DateField(
        'date written')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['author']
        get_latest_by = 'founded_date'

    def __str__(self):
        return "{}:{}".format(
            self.name, self.author)

    def get_absolute_url(self):
        return reverse('collection_poem_detail',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('collection_poem_update',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('collection_poem_delete',
                       kwargs={'slug': self.slug})

    def get_contact_url(self):
        return reverse('contact',
                       kwargs={'slug': self.slug})


class NewsLink(models.Model):
    """Attributes"""

    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    poem = models.ForeignKey(
            Poem,
            null=True,
            on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{}:{}".format(
            self.poem, self.title)

    def get_absolute_url(self):
        return self.poem.get_absolute_url()

    def get_update_url(self):
        return reverse('collection_newslink_update',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('collection_newslink_delete',
                       kwargs={'slug': self.slug})
