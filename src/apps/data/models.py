from django.db import models
from test.test_imageop import MAX_LEN

# Create your models here.
class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    
    def __unicode__(self):
        return u"%s - %s" %(self.title, self.created)
