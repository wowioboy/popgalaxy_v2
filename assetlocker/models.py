from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User


class Asset(models.Model):
    title = models.CharField('Title of Asset',max_length=255)
    asset_date = models.DateTimeField('Upload Date',auto_now_add=True)
    thefile = models.ImageField(verbose_name='Image Asset',upload_to='assets',help_text='Dimensions = Up to YOU!',blank=True,null=True)

    class Meta:
        ordering = ['-asset_date','title']
        verbose_name = "Media Asset"
        verbose_name_plural = "Media Assets"

    def __unicode__(self):
        return self.title

#    @permalink
    def get_absolute_url(self):
        return "http://localhost:8000/media/%s" % (self.thefile,)

