import datetime
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from blog.fields import ThumbnailImageField, WYWIWYGField, FeaturedThumbnailImageField
from blog.models import *
from shows.models import *

class ManyToManyField_NoSyncdb(models.ManyToManyField):
    def __init__(self, *args, **kwargs):
        super(ManyToManyField_NoSyncdb, self).__init__(*args, **kwargs)
        self.creates_table = False

class Video(models.Model):
    isactive = models.BooleanField('Is Active On Site?',default=True)
    featured = models.BooleanField('Featured Video?',default=False)
    carousel = models.BooleanField('Show in Carousel?',default=False)
    spotlight = models.BooleanField('Show in Spotlight List?',default=False)
    incomics = models.BooleanField('Show in Comics?',default=True)
    inmusic = models.BooleanField('Show in Music?',default=True)
    ingames = models.BooleanField('Show in Games?',default=True)
    infilm = models.BooleanField('Show in Film?',default=True)
    intv = models.BooleanField('Show in TV?',default=True)
    inint = models.BooleanField('Show in Interactive?',default=True)
    inextra = models.BooleanField('Show in Extra?',default=True)
    thumbnail = ThumbnailImageField("Thumbnail Image",upload_to='thumbs',help_text='Dimensions = 200x113')
    featuredthumb = FeaturedThumbnailImageField("Featured Image",upload_to='thumbs/featured/video',help_text='Dimensions = 640x360',blank=True,null=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=200,blank=True,null=True)
    carousel_text = models.CharField('Featured Title',max_length=25,blank=True,null=True)
    carousel_subtext = models.CharField('Feature Sub-title',max_length=15,blank=True,null=True)
    duration = models.CharField("Video Duration",max_length=20,blank=True,null=True)
    director = models.CharField("Director",max_length=255,blank=True,null=True)
    producer = models.CharField("Producer / Studio",max_length=255,blank=True,null=True)
    details = WYWIWYGField(verbose_name="Content")
    show = models.ForeignKey(Show,related_name='relatedvideos',blank=True,null=True)
    related_videos = models.ManyToManyField("self",blank=True,null=True)
    url_home = models.TextField('Homepage Embed URL',blank=True,null=True)
    url = models.TextField('Detail Embed URL',blank=True,null=True)
    wowio = models.BooleanField('Available on WOWIO?',default=True)
    wevolt = models.BooleanField('Available on WEVolt?',default=True)
    drunkduck = models.BooleanField('Available on DrunkDuck?',default=True)
    syndicate = models.BooleanField('Available for Syndication?',default=True)
    pub_date = models.DateTimeField('Published Date',blank=True,null=True)
    tags = TagAutocompleteField('Tags',help_text='Keywords to help searching for content.')
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title. -- DO NOT MODIFY',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __unicode__(self):
        return self.title

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    def get_tags(self):
        return Tag.objects.get_for_object(self)

#    @permalink
    def get_absolute_url(self):
        return "/video/%s/" % (self.slug,)
#        return ("video_detail", None, {'slug':self.slug})

#class ViewCount(models.Model):
#    video = models.ForeignKey(Video,related_name='relatedviews')
#    viewcount = models.IntegerField(max_length=8)
#
#    class Meta:
#        verbose_name = ''

class RelatedBlogs(models.Model):
    video = models.ForeignKey(Video,related_name='relatedblogs')
    blog = models.ForeignKey(Entry)

    class Meta:
        verbose_name = 'Related Blog Entry'
        verbose_name_plural = 'Related Blogs'

    def __unicode__(self):
        return u'%s' %(self.blog)


class RelatedLinks(models.Model):
    video = models.ForeignKey(Video,related_name='relatedlinks')
    linkname = models.CharField('Name', max_length=100)
    url = models.URLField('URL', max_length=255)

    class Meta:
        verbose_name = 'Related Link'
        verbose_name_plural = 'Related Links'

    def __unicode__(self):
        return u'%s' %(self.linkname)

