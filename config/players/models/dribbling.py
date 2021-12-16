from django.db import models


class Dribbling(models.Model):
    offensiveawareness = models.PositiveIntegerField
    tightpossession = models.PositiveIntegerField
    physicalcontact = models.PositiveIntegerField
    ballcontrol = models.PositiveIntegerField
    dribbling = models.PositiveIntegerField
    speed = models.PositiveIntegerField
    acceleration = models.PositiveIntegerField
    stamina = models.PositiveIntegerField
