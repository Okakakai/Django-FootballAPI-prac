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

    # condition
    conditionvalue = models.PositiveIntegerField()

    # scoring
    finishing = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    heading = models.PositiveIntegerField()
    jump = models.PositiveIntegerField()
    curl = models.PositiveIntegerField()
    kickingpower = models.PositiveIntegerField()

    # defensive
    defensiveawareness = models.PositiveIntegerField()
    ballwinning = models.PositiveIntegerField()
    aggression = models.PositiveIntegerField()

    # drobbbling
    offensiveawareness = models.PositiveIntegerField()
    tightpossession = models.PositiveIntegerField()
    physicalcontact = models.PositiveIntegerField()
    ballcontrol = models.PositiveIntegerField()
    dribbling = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    acceleration = models.PositiveIntegerField()
    stamina = models.PositiveIntegerField()

    # gksense
    gk_awareness = models.PositiveIntegerField()
    gk_catching = models.PositiveIntegerField()
    gk_clearing = models.PositiveIntegerField()
    gk_reflexes = models.PositiveIntegerField()
    gk_reach = models.PositiveIntegerField()

    # inverseleg
    weakfootusage = models.PositiveIntegerField()  # 逆足頻度
    weakfootaccuracy = models.PositiveIntegerField()  # 逆足精度

    def __str__(self):
        return f"{self.playername} {self.nationality}"
