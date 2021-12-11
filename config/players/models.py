from django.db import models

import uuid

class Player(models.Model):
    # player Model

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    playername = models.CharField(max_length=200)
    age = models.IntegerField(null = False)
    nationality = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    # To discrimination on admin page
    def __str__(self):
        return f"{self.playername} {self.nationality}"