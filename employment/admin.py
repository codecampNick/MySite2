from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'type']


class AccomplishmentsAdmin(admin.ModelAdmin):
    list_display = ['title','company_name']


class ResponsibilitiesAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'company_name']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Accomplishments, AccomplishmentsAdmin)
admin.site.register(Responsibilities, ResponsibilitiesAdmin)
