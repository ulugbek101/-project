from atexit import register
from django.contrib import admin

from . import models

# @admin.register(models.Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('title',)
#     ordering = ('id',)
    
    
admin.site.register(models.Project)
admin.site.register(models.Review)
admin.site.register(models.Tag)
    
