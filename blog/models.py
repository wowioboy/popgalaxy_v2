from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap
import markdown
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from blog.fields import ThumbnailImageField, WYWIWYGField
from profiles.models import *
from shows.models import *

PUB_STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
)
class Entry(models.Model):
    carousel = models.BooleanField('Featured Blog?',default=False)
    incomics = models.BooleanField('Show in Comics?',default=True)
    inmusic = models.BooleanField('Show in Music?',default=True)
    ingames = models.BooleanField('Show in Games?',default=True)
    infilm = models.BooleanField('Show in Film?',default=True)
    intv = models.BooleanField('Show in TV?',default=True)
    inint = models.BooleanField('Show in Interactive?',default=True)
    inextra = models.BooleanField('Show in Extra?',default=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile)
    show = models.ForeignKey(Show,related_name='relatedblogs',blank=True,null=True)
    subtitle = models.CharField(max_length=200,blank=True,null=True)
    carousel_text = models.CharField('Carousel Text',max_length=25,blank=True,null=True)
    source = models.URLField('Entry Source URL',max_length=255,blank=True,null=True)
    source_copy = models.CharField('Source Sentence', max_length=50,blank=True,null=True)
    carousel_subtext = models.CharField('Carousel Sub-text',max_length=15,blank=True,null=True)
    leadin_html = models.TextField(blank=True,null=True)
    leadin_markdown = models.TextField('Lead-in Content',blank=True,null=True)
    body_html = models.TextField(blank=True,null=True)
    body_markdown = models.TextField('Detailed Entry',blank=True,null=True)
    pub_date = models.DateTimeField('Date Published')
    tags = TagAutocompleteField('Tags',help_text='Keywords to help searching for content.')
    enable_comments = models.BooleanField(default=True)
    status = models.IntegerField('Publish Status',choices=PUB_STATUS, default=0)
    thumbnail = ThumbnailImageField(verbose_name="Small Thumbnail",upload_to='thumbs',help_text='Dimensions = 200x113')
    featuredthumb = FeaturedThumbnailImageField(verbose_name="Featured Image",upload_to='thumbs/featured/blog',help_text='Dimensions = 640x360',blank=True,null=True)
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title. DO NOT MODIFY.',
        blank=True,
        null=True
    )
    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'

    def __unicode__(self):
        return u'%s' %(self.title)

    def get_absolute_url(self):
        return "/blog/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    
    def save(self):
         self.body_html = markdown.markdown(self.body_markdown, safe_mode = False)
         #self.leadin_html = markdown.markdown(self.leadin_markdown, safe_mode = False)
         super(Entry, self).save()

    def get_previous_published(self):
        return self.get_previous_by_pub_date(status__exact=1)

    def get_next_published(self):
        return self.get_next_by_pub_date(status__exact=1)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

class RelatedLinks(models.Model):
    blog = models.ForeignKey(Entry,related_name='relatedlinks')
    linkname = models.CharField('Name', max_length=100)
    url = models.URLField('URL', max_length=255)

    class Meta:
        verbose_name = 'Related Link'
        verbose_name_plural = 'Related Links'

    def __unicode__(self):
        return u'%s' %(self.linkname)
