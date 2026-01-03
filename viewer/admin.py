from django.contrib import admin
from .models import Country, City, Location, Sport, Event

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(Sport)
admin.site.register(Event)