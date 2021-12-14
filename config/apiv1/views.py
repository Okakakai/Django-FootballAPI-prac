from django.db.models import query_utils
from rest_framework import viewsets

from players.models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all().order_by('playername', 'date')
    serializer_class = PlayerSerializer
    filter_fields = ('playername', 'nationality')
