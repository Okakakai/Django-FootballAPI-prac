from rest_framework import serializers

from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'date', 'playername', 'playerimage',
                  'nationality', 'team', 'updated_at')
        read_only_fields = ('id',)
