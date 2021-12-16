from django.db import models


class GkSense(models.Model):
    gk_awareness = models.PositiveIntegerField
    gk_catching = models.PositiveIntegerField
    gk_clearing = models.PositiveIntegerField
    gk_reflexes = models.PositiveIntegerField
    gk_reach = models.PositiveIntegerField
