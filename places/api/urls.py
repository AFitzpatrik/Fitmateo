from django.urls import path
from .views import PlaceListAPIView

urlpatterns = [
    path('places/', PlaceListAPIView.as_view(), name='api_places'),
]
