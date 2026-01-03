from django.conf import settings
from django.db import models
from django.db.models import ForeignKey, DateTimeField

class Country(models.Model): #Stát kde bude událost, příprava pro rožšíření mio ČR
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        error_messages={"unique": "Stát s tímto názvem již existuje."},
    )

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Country(name={self.name})"


class City(models.Model): #Město kde bude událost
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="cities")
    zip_code = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Location(models.Model): #Například hřiště, gym atd.
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    city = ForeignKey(City, on_delete=models.PROTECT, related_name="locations")

    class Meta:
        ordering = ["city__name", "name"]
        unique_together = ("name", "address")

    def __str__(self):
        return self.name

    def __repr__(self):
        city_name = self.city.name if self.city else None
        return f"Location(name={self.name}, city={city_name}, address={self.address})"


class Sport(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        error_messages={"unique": "Sport s tímto názvem již existuje."},
    )
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Event(models.Model): #Inzerát na skupinovou aktivitu
    name = models.CharField(max_length=100,null=False, blank=False)
    sport = models.ForeignKey(Sport, on_delete=models.PROTECT, related_name="events")
    description = models.TextField(null=True, blank=True)
    start_date_time = DateTimeField(null=False, blank=False)
    end_date_time = DateTimeField(null=False, blank=False)
    event_image = models.ImageField(upload_to="event_images/", null=True, blank=True)
    owner_of_event = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name="owned_events")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="events")
    capacity = models.PositiveIntegerField(null=True, blank=True) #None = neomezeno
    created_at = models.DateTimeField(auto_now_add=True) #Přidání pole pro datum vytvoření
    updated_at = models.DateTimeField(auto_now=True)