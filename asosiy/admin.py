from django.contrib import admin
from .models import *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display =("id", "nom", "davlat")
    search_fields = ("nom",)
    list_filter = ("davlat", )

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("ism", "t_yil", "club")
    search_fields = ("ism", )
    list_filter = ("club", )
    autocomplete_fields = ("club", )

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ("id", "player", "eski", "yangi", "mavsum")
    search_fields = ("player__ism", "yangi__nom")
    list_filter = ("mavsum", )
    autocomplete_fields = ("player", "eski", "yangi")

admin.site.register(Hozirgi_mavsum)