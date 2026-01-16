from rest_framework import generics
from places.models import Place
from .serializers import PlaceSerializer


class PlaceListAPIView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
