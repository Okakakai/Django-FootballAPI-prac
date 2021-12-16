from django.db import models


class Totalvalue(models.Model):
    totalvalue = models.PositiveIntegerField(null=True)
