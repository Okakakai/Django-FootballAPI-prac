from django.db import models


class Scoring(models.Model):
    finishing = models.PositiveIntegerField
    balance = models.PositiveIntegerField
    heading = models.PositiveIntegerField
    jump = models.PositiveIntegerField
    curl = models.PositiveIntegerField
    kickingpower = models.PositiveIntegerField
