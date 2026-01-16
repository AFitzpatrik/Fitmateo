from rest_framework import serializers
from places.models import Place, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    reviews_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'description',
            'latitude',
            'longitude',
            'tags',
            'average_rating',
            'reviews_count',
        )
        read_only_fields = (
            'id',
            'tags',
            'average_rating',
            'reviews_count',
        )

