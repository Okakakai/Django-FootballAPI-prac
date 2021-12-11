from rest_framework import serializers

from players.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id','playername','nationality','team','updated_at')
        read_only_fields = ('id',)