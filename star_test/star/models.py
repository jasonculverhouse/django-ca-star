from django.db import models

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

    