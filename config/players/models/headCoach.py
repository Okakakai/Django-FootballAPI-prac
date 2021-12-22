import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class HeadCoach(models.Model):
    OFFENSIVETYPE_CHOICES = (
        ('OFTYPE_C', 'Counter'),
        ('OFTYPE_P', 'Possessions')
    )
    BUILDUP_CHOICES = (
        ('BUILD_LP', 'LongPass'),
        ('BUILD_SP', 'ShortPass')
    )
    ATTACKAREA_CHOICES = (
        ('ATAREA_S', 'SideArea'),
        ('ATAREA_C', 'CenterArea')
    )
    POSITIONING_CHOICES = (
        ('POS_FLUID', 'Positionfluid'),
        ('POS_FIXED', 'Positionfixed')
    )
    DEFENSIVETYPE_CHOICES = (
        ('DFTYPE_FORE', 'Forecheck'),
        ('DFTYPE_RET', 'Retreat')
    )
    DRIVEINAREA_CHOICES = (
        ('DRIVEIN_C', 'driveinCenter'),
        ('DRIVEIN_S', 'driveinSide')
    )
    PRESSING_CHOICES = (
        ('PRESS_AG', 'pressingAggressive'),
        ('PRESS_SA', 'pressingSafety')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)

    headcoachname = models.CharField(max_length=50)
    headcoachimage = models.ImageField(
        upload_to='images/headcoaches/', default='images/headCoaches/HeadCoachDefaultImage.png')

    managementability = models.PositiveIntegerField(null=False)
    adaptability = models.PositiveIntegerField(null=False)
    formation = models.CharField(max_length=20, null=False)

    formationimage = models.ImageField(
        upload_to='images/headcoaches/', blank=True)

    # Number of people in each position
    cf_number = models.IntegerField(
        default=2, validators=[MinValueValidator(0), MaxValueValidator(4)])
    st_number = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])

    lwg_number = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    rwg_number = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])

    lmf_number = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    rmf_number = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])

    omf_number = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(4)])
    cmf_number = models.IntegerField(
        default=2, validators=[MinValueValidator(0), MaxValueValidator(4)])
    dmf_number = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(4)])

    cb_number = models.IntegerField(
        default=2, validators=[MinValueValidator(0), MaxValueValidator(4)])
    rsb_number = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(4)])
    lsb_number = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(4)])

    gk_number = models.IntegerField(default=1)

    offensivetype = models.CharField(
        max_length=100, choices=OFFENSIVETYPE_CHOICES)
    buildup = models.CharField(max_length=100, choices=BUILDUP_CHOICES)
    attackarea = models.CharField(
        max_length=100, choices=ATTACKAREA_CHOICES)
    positioning = models.CharField(
        max_length=100, choices=POSITIONING_CHOICES)
    defensivetype = models.CharField(
        max_length=100, choices=DEFENSIVETYPE_CHOICES)
    driveinarea = models.CharField(
        max_length=100, choices=DRIVEINAREA_CHOICES
    )
    pressing = models.CharField(max_length=100, choices=PRESSING_CHOICES)

    def __str__(self):
        return f"{self.headcoachname}"
