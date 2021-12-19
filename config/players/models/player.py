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
    totalvalue = models.PositiveIntegerField(null=True)

    offensiveawareness = models.PositiveIntegerField()
    ballcontrol = models.PositiveIntegerField()
    dribbling = models.PositiveIntegerField()
    tightpossession = models.PositiveIntegerField()

    lowpass = models.PositiveIntegerField()
    loftedpass = models.PositiveIntegerField()

    finishing = models.PositiveIntegerField()
    heading = models.PositiveIntegerField()
    placekicking = models.PositiveIntegerField()
    curl = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    acceleration = models.PositiveIntegerField()
    kickingpower = models.PositiveIntegerField()
    jump = models.PositiveIntegerField()
    physicalcontact = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    stamina = models.PositiveIntegerField()
    defensiveawareness = models.PositiveIntegerField()
    ballwinning = models.PositiveIntegerField()
    aggression = models.PositiveIntegerField()

    gk_awareness = models.PositiveIntegerField()
    gk_catching = models.PositiveIntegerField()
    gk_clearing = models.PositiveIntegerField()
    gk_reflexes = models.PositiveIntegerField()
    gk_reach = models.PositiveIntegerField()
    weakfootusage = models.PositiveIntegerField()
    weakfootaccuracy = models.PositiveIntegerField()
    conditionvalue = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.playername} {self.nationality}"
