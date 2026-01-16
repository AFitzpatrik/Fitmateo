from decimal import Decimal

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Avg


def validate_half_step(value):
    if (value * Decimal('2')) % 1 != 0:
        raise ValidationError('Rating must be in 0.5 steps')


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    PLACE_TYPE_CHOICES = [
        ('kickbox', 'Kickbox'),
        ('box', 'Box'),
        ('mma', 'MMA'),
        ('muaythai', 'Muay Thai'),
        ('bodybuilding', 'Bodybuilding'),
        ('fitness', 'Fitness'),
    ]

    place_type = models.CharField(
        max_length=20,
        choices=PLACE_TYPE_CHOICES,
        default='fitness',
        db_index=True
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tags = models.ManyToManyField(Tag, related_name='places', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        avg = self.reviews.aggregate(avg=Avg('rating'))['avg']
        if avg is None:
            return 0
        return round(avg * 2) / 2

    def reviews_count(self):
        return self.reviews.count()

    def __str__(self):
        return self.name


class Review(models.Model):
    place = models.ForeignKey(
        Place,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
            validate_half_step
        ]
    )
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('place', 'user')

    def __str__(self):
        return f'{self.place.name} - {self.rating}'
