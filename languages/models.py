from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    experience_level = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

