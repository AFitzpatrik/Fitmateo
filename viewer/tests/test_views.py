from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

from viewer.models import Country, City, Sport, Location, Event, Region


class EventListViewTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            password="test12345"
        )

        self.country = Country.objects.create(name="Česká republika")
        self.region = Region.objects.create(name="Hlavní město Praha")

        self.city = City.objects.create(
            name="Praha",
            country=self.country,
            zip_code="11000",
            region=self.region
        )

        self.location = Location.objects.create(
            name="Gym",
            description="Test gym",
            address="Test adresa",
            city=self.city
        )

        self.sport = Sport.objects.create(name="Tenis")

        self.event = Event.objects.create(
            name="Test event",
            sport=self.sport,
            description="Popis",
            start_date_time=timezone.now(),
            end_date_time=timezone.now(),
            owner_of_event=self.user,
            location=self.location,
            capacity=10
        )

    def test_event_list_view_status_code(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)

    def test_event_list_view_uses_correct_template(self):
        response = self.client.get(reverse("events"))
        self.assertTemplateUsed(response, "events.html")

    def test_event_list_contains_event(self):
        response = self.client.get(reverse("events"))
        self.assertIn(self.event, response.context["events"])
