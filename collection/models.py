from django.db import models
from django.urls import reverse

# Create your models here.


class Tag(models.Model):
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

    # def get_absolute_url(self):
    #     return reverse('organizer_tag_detail',
    #                    kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('organizer_tag_update',
    #                    kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('organizer_tag_delete',
    #                    kwargs={'slug': self.slug})


class Poem(models.Model):
    name = models.CharField(
        max_length=31, db_index=True)
    name_author = models.CharField(
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
        ordering = ['name_author']
        get_latest_by = 'written_date'

    def __str__(self):
        return "{}:{}".format(
            self.poem, self.name_author)
#        return self.name + '\n' + self.name_author

    # def get_absolute_url(self):
    #     return reverse('organizer_startup_detail',
    #                    kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse('organizer_startup_update',
    #                    kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('organizer_startup_delete',
    #                    kwargs={'slug': self.slug})


class NewsLink(models.Model):
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
#        unique_together = ('slug', 'startup')

    def __str__(self):
        return "{}:{}".format(
            self.poem, self.title)

    # def get_absolute_url(self):       
    #     return self.startup.get_absolute_url()

    # def get_update_url(self):
    #     return reverse('organizer_newslink_update',
    #                    kwargs={'slug': self.slug})
    #     # return reverse(
    #     #     'organizer_newslink_update',
    #     #     kwargs={'pk': self.pk})

    # def get_delete_url(self):
    #     return reverse('organizer_newslink_delete',
    #                    kwargs={'slug': self.slug})
    #     # return reverse(
    #     #     'organizer_newslink_delete',
    #     #     kwargs={'pk': self.pk})
