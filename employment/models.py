from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    type = models.CharField(max_length=100)
    company_description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Accomplishments(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    company_name = models.ForeignKey(Company, on_delete=models.PROTECT)
    rank = models.SmallIntegerField()


class Responsibilities(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.CharField(max_length=4000, null=True, blank=True)
    company_name = models.ForeignKey(Company, on_delete=models.PROTECT)
