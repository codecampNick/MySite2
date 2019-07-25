from django.db import models
from languages.models import Language

class Project(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    short_description = models.CharField(max_length=255, default='Need Short Description')
    description = models.CharField(max_length=8000)
    created = models.BooleanField(default=False)
    is_active = models.BooleanField(default=1)
