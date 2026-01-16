import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Place


def map_view(request):
    return render(request, 'map.html')


def places_list_api(request):
    places = Place.objects.all()
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
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def place_create_api(request):
    print("🔥 PLACE CREATE API HIT 🔥")
    import json

    body = json.loads(request.body.decode('utf-8'))

    place = Place.objects.create(
        name=body.get('name'),
        description=body.get('description', ''),
        latitude=body.get('latitude'),
        longitude=body.get('longitude'),
        place_type=body.get('place_type', 'fitness'),
    )

    return JsonResponse({
        'id': place.id,
        'name': place.name,
        'description': place.description,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'place_type': place.place_type,
    }, status=201)