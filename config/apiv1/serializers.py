from rest_framework import serializers

from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'date', 'playername', 'totalvalue', 'playerimage',
                  'nationality', 'team', 'updated_at')
        read_only_fields = ('id',)


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'date', 'nationality', 'playerimage', 'totalvalue', 'playername', 'mostsuitableposition_type',
                  'suitableposition_type')