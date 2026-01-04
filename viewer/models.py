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
        verbose_name="Název",
    )

    class Meta:
        verbose_name = "Stát"
        verbose_name_plural = "Státy"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Country(name={self.name})"


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Název")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class City(models.Model): #Město kde bude událost
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Název")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="cities", verbose_name="Název")
    zip_code = models.CharField(max_length=10, null=False, blank=False, verbose_name="PSČ")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name="cities", verbose_name="Kraj")

    class Meta:
        verbose_name = "Město"
        verbose_name_plural = "Města"
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Location(models.Model): #Například hřiště, gym atd.
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Název")
    description = models.TextField(null=False, blank=False, verbose_name="Popis")
    address = models.TextField(null=False, blank=False,verbose_name="Adresa")
    city = ForeignKey(City, on_delete=models.PROTECT, related_name="locations", verbose_name="Město")

    class Meta:
        verbose_name = "Lokace"
        verbose_name_plural = "Lokace"
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
        verbose_name="Název"
    )

    class Meta:
        verbose_name = "Sport"
        verbose_name_plural = "Sporty"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Event(models.Model): #Inzerát na skupinovou aktivitu
    name = models.CharField(max_length=100,null=False, blank=False, verbose_name="Název")
    sport = models.ForeignKey(Sport, on_delete=models.PROTECT, related_name="events", verbose_name="Sport")
    description = models.TextField(null=True, blank=True, verbose_name="Popis")
    start_date_time = DateTimeField(null=False, blank=False, verbose_name="Datum a čas začátku")
    end_date_time = DateTimeField(null=False, blank=False, verbose_name="Datum a čas konce")
    event_image = models.ImageField(upload_to="event_images/", null=True, blank=True, verbose_name="Obrázek")
    owner_of_event = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name="owned_events", verbose_name="Majitel události")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="events", verbose_name="Lokace")
    capacity = models.PositiveIntegerField(null=True, blank=True, verbose_name="Kapacita") #None = neomezeno
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Datum vytvoření") #Přidání pole pro datum vytvoření
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Datum upravení")

    class Meta:
        verbose_name = "Událost"
        verbose_name_plural = "Události"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name