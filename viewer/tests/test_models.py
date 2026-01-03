from django.test import TestCase
from viewer.models import Country, City, Sport, Location, Event
from django.contrib.auth import get_user_model
from django.utils import timezone

class CountryModelTest(TestCase):

    def test_create_country(self):
        country = Country.objects.create(name="Česká republika")
        self.assertEqual(country.name, "Česká republika")

    def test_country_str(self):
        country = Country.objects.create(name="Slovensko")
        self.assertEqual(str(country), "Slovensko")


class CityModelTest(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Česká republika")

    def test_create_city(self):
        city = City.objects.create(
            name="Praha",
            country=self.country,
            zip_code="11000"
        )

        self.assertEqual(city.name, "Praha")
        self.assertEqual(city.country.name, "Česká republika")

    def test_city_str(self):
        city = City.objects.create(
            name="Brno",
            country=self.country,
            zip_code="60200"
        )
        self.assertEqual(str(city), "Brno")


class SportModelTest(TestCase):

    def test_create_sport(self):
        sport = Sport.objects.create(name="Box")
        self.assertEqual(sport.name, "Box")

    def test_sport_str(self):
        sport = Sport.objects.create(name="MMA")
        self.assertEqual(str(sport), "MMA")


class LocationModelTest(TestCase):

    def setUp(self):
        self.country = Country.objects.create(name="Česká republika")
        self.city = City.objects.create(
            name="Praha",
            country=self.country,
            zip_code="11000"
        )

    def test_create_location(self):
        location = Location.objects.create(
            name="Fitness centrum",
            description="Moderní gym",
            address="Václavské náměstí 1",
            city=self.city
        )

        self.assertEqual(location.city.name, "Praha")


class EventModelTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.cz",
            password="test12345"
        )

        self.country = Country.objects.create(name="Česká republika")
        self.city = City.objects.create(
            name="Praha",
            country=self.country,
            zip_code="11000"
        )

        self.location = Location.objects.create(
            name="Gym",
            description="Test gym",
            address="Test adresa",
            city=self.city
        )

        self.sport = Sport.objects.create(name="Box")

    def test_create_event(self):
        event = Event.objects.create(
            name="Ranní box",
            sport=self.sport,
            description="Lehký trénink",
            start_date_time=timezone.now(),
            end_date_time=timezone.now(),
            owner_of_event=self.user,
            location=self.location,
            capacity=10
        )

        self.assertEqual(event.sport.name, "Box")
        self.assertEqual(event.owner_of_event.email, "test@test.cz")

