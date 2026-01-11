from django.shortcuts import render
from django.views.generic import ListView

from viewer.models import Event


class EventListView(ListView):
    template_name = 'viewer/templates/events.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 9
    ordering = ["name"] #Prozatím dle jména, později dle data nejblížeší události


class EventDetailView(ListView):
    template_name = 'viewer/templates/event_detail.html'
    model = Event
    context_object_name = 'event'
#    # Základní implementace, bude potřeba upravit pro detail události

