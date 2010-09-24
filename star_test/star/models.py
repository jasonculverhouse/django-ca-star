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

class Entity(models.Model):
    county_code = models.IntegerField()
    district_code = models.IntegerField()
    school_code = models.IntegerField()
    charter_number = models.IntegerField()
    test_year = models.IntegerField()

    TYPE_ID_CHOICES = (
        (4, 'State'),
        (5, 'County'),
        (6, 'District'),
        (7, 'School'),
        (9, 'Independent Charter School'),
        (10, 'Dependent Charter School'),
    )
    
    type_id = models.IntegerField(choices=TYPE_ID_CHOICES)
    county_name = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255, null=True)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.school_name, self.district_name, self.county_name)
    
    