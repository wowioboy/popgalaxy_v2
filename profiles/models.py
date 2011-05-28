from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from blog.fields import ThumbnailImageField, WYWIWYGField, FeaturedThumbnailImageField
import markdown


class Profile(models.Model):
    thumbnail = ThumbnailImageField("Profile Image",upload_to='shows/hosts',blank=True,null=True)
    name = models.CharField('Username or Handle',max_length=255)
    twitter = models.CharField('Twitter Handle',max_length=200,blank=True,null=True)
    facebook_url = models.CharField('Facebook URL',max_length=200,blank=True,null=True)
    bio_html = models.TextField(blank=True,null=True)
    bio_markdown = WYWIWYGField('Brief Bio',blank=True,null=True)
    tags = TagAutocompleteField('Tags',help_text='Keywords to help searching for content.')
    slug = models.SlugField(
        help_text='Automatically built from the title. -- DO NOT MODIFY',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Host Profile"
        verbose_name_plural = "Host Profiles"

    def __unicode__(self):
        return self.name

    def get_tags(self):
        return Tag.objects.get_for_object(self)

#    @permalink
    def get_absolute_url(self):
        return "/profiles/%s/" % (self.slug,)

    def save(self):
         self.bio_html = markdown.markdown(self.bio_markdown, safe_mode = False)
         super(Profile, self).save()
