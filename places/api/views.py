from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from places.models import Place, Tag
from .serializers import PlaceSerializer


@api_view(['GET'])
def places_list_api(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(
        places,
        many=True,
        context={'request': request}
    )
    return Response(serializer.data)


@api_view(['POST'])
def place_create_api(request):
    print('🔥 PLACE CREATE API HIT 🔥')

    name = request.data.get('name')
    description = request.data.get('description', '')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    place_type = request.data.get('place_type', 'fitness')
    image = request.FILES.get('image')

    tags_raw = request.data.getlist('tags[]')

    place = Place.objects.create(
        name=name,
        description=description,
        latitude=latitude,
        longitude=longitude,
        place_type=place_type,
        image=image
    )

    for tag_name in tags_raw:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        place.tags.add(tag)

    serializer = PlaceSerializer(
        place,
        context={'request': request}
    )
    return Response(serializer.data, status=status.HTTP_201_CREATED)
