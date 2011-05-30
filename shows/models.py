from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from blog.fields import ThumbnailImageField, WYWIWYGField, ShowThumbnailImageField
from tagging.fields import TagField
from tagging.models import Tag
import markdown


class Show(models.Model):
    isactive = models.BooleanField('Is Show Active On Site?',default=True,)
    title = models.CharField('Title of Show',max_length=255)
    body_html = models.TextField(blank=True,null=True)
    body_markdown = WYWIWYGField('Brief Description',blank=True,null=True)
    stylesheet = models.CharField('CSS Stylesheet', max_length=100, help_text='Specify the name of the stylesheet. INCLUDE the extension.',blank=True,null=True)
    schedule = models.CharField('Update Schedule', max_length=50, help_text='Specify day of the week that this show is updated.',blank=True,null=True)
    thumbnail = ShowThumbnailImageField(verbose_name="Logo Image",upload_to='shows',help_text='Dimensions = 200x113',blank=True,null=True)
    facebook_url = models.CharField('Facebook URL', max_length=150,blank=True,null=True)
    twitter_url = models.CharField('Twitter URL', max_length=150,blank=True,null=True)
    reddit_url = models.CharField('Reddit URL', max_length=150,blank=True,null=True)
    youtube_url = models.CharField('Youtube URL', max_length=150,blank=True,null=True)
    tags = TagField()
    slug = models.SlugField(
        help_text='Automatically built from the title. -- DO NOT MODIFY',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['title']
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __unicode__(self):
        return self.title

#    @permalink
    def get_absolute_url(self):
        return "/show/%s/" % (self.slug,)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def save(self):
         self.body_html = markdown.markdown(self.body_markdown, safe_mode = False)
         super(Show, self).save()
