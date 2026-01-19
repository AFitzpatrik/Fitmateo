from django.urls import path
from .views import (
    map_view,
    places_list_api,
    place_create_api,
)

urlpatterns = [
    path('map/', map_view, name='map'),

    path('api/places/', places_list_api, name='api_places'),
    path('api/places/create/', place_create_api, name='api_places_create'),
]
