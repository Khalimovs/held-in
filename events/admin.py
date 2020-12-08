from django.contrib import admin

from .models import Event, Reference, Contestant, Winner, Project

admin.site.register(Event)
admin.site.register(Reference)
admin.site.register(Contestant)
admin.site.register(Winner)
admin.site.register(Project)


