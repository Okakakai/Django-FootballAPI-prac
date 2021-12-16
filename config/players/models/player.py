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

    def __str__(self):
        return f"{self.playername} {self.nationality}"
