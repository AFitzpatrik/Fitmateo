from django.urls import path
from .views import PlaceListAPIView, PlaceCreateAPIView

urlpatterns = [
    path('places/', PlaceListAPIView.as_view(), name='api_places'),
    path('places/create/', PlaceCreateAPIView.as_view(), name='api_place_create'),
]
