from django.db import models


class InverseLeg(models.Model):
    weakfootusage = models.PositiveIntegerField  # 逆足頻度
    weakfootaccuracy = models.PositiveIntegerField  # 逆足精度
