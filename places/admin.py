from django.contrib import admin

from .models import Place, Tag, Review


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    ordering = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'place_type',
        'average_rating_display',
        'reviews_count_display',
        'tags_display',
        'created_at',
    )

    list_filter = ('place_type', 'tags')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

    filter_horizontal = ('tags',)

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'description',
                'place_type',
                'image',
            )
        }),
        ('Lokace', {
            'fields': (
                'latitude',
                'longitude',
            )
        }),
        ('Tagy (max 10)', {
            'fields': ('tags',)
        }),
    )

    def average_rating_display(self, obj):
        return obj.average_rating()
    average_rating_display.short_description = 'Hodnocení'

    def reviews_count_display(self, obj):
        return obj.reviews_count()
    reviews_count_display.short_description = 'Počet recenzí'

    def tags_display(self, obj):
        return ', '.join(f'#{tag.name}' for tag in obj.tags.all())
    tags_display.short_description = 'Tagy'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        tags = obj.tags.all()
        if tags.count() > 10:
            obj.tags.set(tags[:10])


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'place',
        'user',
        'rating',
        'created_at',
    )

    list_filter = ('rating', 'created_at')
    search_fields = ('place__name', 'user__username')
    ordering = ('-created_at',)
