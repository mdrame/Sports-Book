from django.contrib import admin
from soccer.models import Team

#
# class TeamAdmin(admin.ModelAdmin):
#     """ Show helpful fields on the changelist page. """
#     list_display = ('title', 'slug', 'author', 'created', 'modified')


admin.site.register(Team)
