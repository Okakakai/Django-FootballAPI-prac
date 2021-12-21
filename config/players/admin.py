from django.contrib import admin

from .models import Player
from .models import HeadCoach


class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ('playername', 'nationality', 'id', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')


admin.site.register(Player, PlayerModelAdmin)


class HeadCoachModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'managementability', 'id', 'created_at')
    ordering = ('managementability',)
    readonly_fields = ('id', 'created_at')


admin.site.register(HeadCoach, HeadCoachModelAdmin)
