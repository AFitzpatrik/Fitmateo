from django.shortcuts import render
from django.views.generic import ListView

from viewer.models import Event


class EventListView(ListView):
    template_name = 'viewer/events.html'
    model = Event
    context_object_name = 'events'
    paginate_by = 9

