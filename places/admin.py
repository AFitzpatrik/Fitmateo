from django.contrib import admin
from .models import Place, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_rating', 'reviews_count')
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('place', 'user', 'rating', 'created_at')
