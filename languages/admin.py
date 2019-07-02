from django.contrib import admin
from . models import *


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','experience_level')


admin.site.register(Language, LanguageAdmin)
