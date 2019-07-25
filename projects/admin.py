from django.contrib import admin
from . models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'short_description', 'created')

admin.site.register(Project, ProjectAdmin)
