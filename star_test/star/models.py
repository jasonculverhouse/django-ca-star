from django.db import models

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

class SubGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    sub_group = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['category', 'sub_group']
    
    def __unicode__(self):
        return u'%s (%s)' % (self.sub_group, self.category)
    