from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from places.models import Place
from .serializers import PlaceSerializer


class PlaceListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class PlaceCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print('POST DATA:', request.data)

        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            place = serializer.save()
            return Response(
                PlaceSerializer(place).data,
                status=status.HTTP_201_CREATED
            )

        print('ERRORS:', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
