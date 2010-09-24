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


TYPE_ID_CHOICES = (
    (4, 'State'),
    (5, 'County'),
    (6, 'District'),
    (7, 'School'),
    (9, 'Independent Charter School'),
    (10, 'Dependent Charter School'),
)

class County(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type_id = models.IntegerField(choices=TYPE_ID_CHOICES)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return u'%s' % self.name

class District(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return u'%s' % self.name

class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    district = models.ForeignKey('District')
    county = models.ForeignKey('County')
    charter_number = models.IntegerField(null = True)
    type_id = models.IntegerField(choices=TYPE_ID_CHOICES)
    test_year = models.IntegerField()
    zipcode = models.CharField(max_length=255, null=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return u'%s' % self.name
    
class Entity(models.Model):
    county = models.ForeignKey('County')
    district = models.ForeignKey('District', null = True)
    school = models.ForeignKey('School', null = True)
    charter_number = models.IntegerField(null = True)
    test_year = models.IntegerField(null=True)
    type_id = models.IntegerField(choices=TYPE_ID_CHOICES)
    zipcode = models.CharField(max_length=255, null=True)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.school_name, self.district_name, self.county_name)

class Score(models.Model):
    county = models.ForeignKey('County')
    district = models.ForeignKey('District', null = True)
    school = models.ForeignKey('School', null = True)
    charter_number = models.IntegerField()
    test_year = models.IntegerField()
    subgroup = models.ForeignKey(SubGroup)

    TYPE_TYPE_CHOICES = (
        ('C', 'CST'),
        ('M', 'CMA'),
        ('P', 'CAPA'),
        ('S', 'STA'),
    )
    test_type = models.CharField(choices = TYPE_TYPE_CHOICES, max_length=1)
    capa_assessment_level = models.IntegerField()
    total_star_enrollment = models.IntegerField()
    total_tested_at_entity_level = models.IntegerField()
    total_tested_at_subgroup_level = models.IntegerField()
    grade = models.IntegerField()
    test = models.ForeignKey(Test)
    star_reported_enrollment_capa_eligible = models.IntegerField(null = True)
    students_tested = models.IntegerField()
    percent_tested = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    mean_scale_score = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    percentage_advanced = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    percentage_proficient = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    percentage_at_or_above_proficient = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    percentage_basic = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    percentage_below_basic = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    percentage_far_below_basic = models.DecimalField(max_digits=5, decimal_places=2, null = True)
    students_with_scores = models.IntegerField()
    cma_sts_average_percent_correct = models.DecimalField(max_digits=5, decimal_places=2, null = True)\
