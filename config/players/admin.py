from django.contrib import admin

from .models import Player

class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ('playername','nationality','id','created_at')
    ordering = ('-created_at',)
    readonly_fields = ('id','created_at')


admin.site.register(Player, PlayerModelAdmin)
