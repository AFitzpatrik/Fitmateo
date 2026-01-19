import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import Prefetch

from .models import Place, Tag


def map_view(request):
    return render(request, 'map.html')


def places_list_api(request):
    places = (
        Place.objects
        .prefetch_related('tags', 'reviews')
        .all()
    )

    data = []

    for place in places:
        data.append({
            'id': place.id,
            'name': place.name,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'place_type': place.place_type,
            'average_rating': place.average_rating(),
            'reviews_count': place.reviews_count(),
            'image': place.image.url if place.image else None,
            'tags': [tag.name for tag in place.tags.all()],
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def place_create_api(request):
    body = json.loads(request.body.decode('utf-8'))

    name = body.get('name')
    description = body.get('description', '')
    latitude = body.get('latitude')
    longitude = body.get('longitude')
    place_type = body.get('place_type', 'fitness')
    tags_input = body.get('tags', [])

    if not name or latitude is None or longitude is None:
        return JsonResponse(
            {'error': 'Missing required fields'},
            status=400
        )

    place = Place.objects.create(
        name=name,
        description=description,
        latitude=latitude,
        longitude=longitude,
        place_type=place_type,
    )

    # TAGY – max 10
    if isinstance(tags_input, list):
        for tag_name in tags_input[:10]:
            tag_name = tag_name.strip().lower()
            if not tag_name:
                continue

            tag, _ = Tag.objects.get_or_create(name=tag_name)
            place.tags.add(tag)

    return JsonResponse({
        'id': place.id,
        'name': place.name,
        'description': place.description,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'place_type': place.place_type,
        'image': place.image.url if place.image else None,
        'tags': [tag.name for tag in place.tags.all()],
        'average_rating': 0,
        'reviews_count': 0,
    }, status=201)
