from django.db import models


class Defensive(models.Model):
    defensiveawareness = models.PositiveIntegerField
    ballwinning = models.PositiveIntegerField
    aggression = models.PositiveIntegerField
