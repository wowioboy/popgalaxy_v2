from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    
    author = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    def __unicode__(self):
        return 'Comment: ' + str(self.id)
    
    class Meta:
        
        ordering = ('-date_added',)