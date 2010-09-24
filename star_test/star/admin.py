from star_test.star import models
from django.contrib import admin

admin.site.register(models.Test)

class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('sub_group', 'category')
    list_filter = ['category']
    
admin.site.register(models.SubGroup, SubGroupAdmin)
    