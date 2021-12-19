import uuid

from django.db import models


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(blank=False)
    playername = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=False)
    height = models.PositiveIntegerField(null=False)
    nationality = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    playerimage = models.ImageField(upload_to='images/', blank=True)

    # Total
    totalvalue = models.PositiveIntegerField(null=False)

    offensiveawareness = models.PositiveIntegerField(null=False)
    ballcontrol = models.PositiveIntegerField(null=False)
    dribbling = models.PositiveIntegerField(null=False)
    tightpossession = models.PositiveIntegerField(null=False)

    lowpass = models.PositiveIntegerField(null=False)
    loftedpass = models.PositiveIntegerField(null=False)

    finishing = models.PositiveIntegerField(null=False)
    heading = models.PositiveIntegerField(null=False)
    placekicking = models.PositiveIntegerField(null=False)
    curl = models.PositiveIntegerField(null=False)
    speed = models.PositiveIntegerField(null=False)
    acceleration = models.PositiveIntegerField(null=False)
    kickingpower = models.PositiveIntegerField(null=False)
    jump = models.PositiveIntegerField(null=False)
    physicalcontact = models.PositiveIntegerField(null=False)
    balance = models.PositiveIntegerField(null=False)
    stamina = models.PositiveIntegerField(null=False)
    defensiveawareness = models.PositiveIntegerField(null=False)
    ballwinning = models.PositiveIntegerField(null=False)
    aggression = models.PositiveIntegerField(null=False)

    gk_awareness = models.PositiveIntegerField(default=40)
    gk_catching = models.PositiveIntegerField(default=40)
    gk_clearing = models.PositiveIntegerField(default=40)
    gk_reflexes = models.PositiveIntegerField(default=40)
    gk_reach = models.PositiveIntegerField(default=40)

    weakfootusage = models.PositiveIntegerField(null=False)
    weakfootaccuracy = models.PositiveIntegerField(null=False)
    conditionvalue = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.playername} {self.nationality}"
