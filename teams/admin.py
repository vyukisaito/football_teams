from django.contrib import admin
from teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'year', 'country', 'city', )
    search_fields = ('team', )


admin.site.register(Team, TeamAdmin)
