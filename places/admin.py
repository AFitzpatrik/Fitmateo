from django.contrib import admin
from .models import Place, Review, Tag


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_rating', 'reviews_count')
    list_filter = ('tags',)
    search_fields = ('name',)
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('place', 'user', 'rating', 'created_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
