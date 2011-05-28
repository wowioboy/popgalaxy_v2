from django.db import models

class Headline(models.Model):
    isactive = models.BooleanField('Is Active On Site?',default=True)
    incomics = models.BooleanField('Show in Comics?',default=True)
    inmusic = models.BooleanField('Show in Music?',default=True)
    ingames = models.BooleanField('Show in Games?',default=True)
    infilm = models.BooleanField('Show in Film?',default=True)
    intv = models.BooleanField('Show in TV?',default=True)
    inint = models.BooleanField('Show in Interactive?',default=True)
    inextra = models.BooleanField('Show in Extra?',default=True)
    title = models.CharField('Headline', max_length=255)
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'headlines'

    def __unicode__(self):
        return u'%s' %(self.title)
