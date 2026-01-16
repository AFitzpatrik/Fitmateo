from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from places.models import Place
from .serializers import PlaceSerializer


class PlaceListAPIView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny]


@method_decorator(csrf_exempt, name='dispatch')
class PlaceCreateAPIView(generics.CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
