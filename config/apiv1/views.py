from django.db.models import query_utils
from rest_framework import viewsets

from players.models import Player
from .serializers  import PlayerSerializer
from apiv1 import serializers

class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer