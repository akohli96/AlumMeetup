from meetup.repository.models import *
from django.test import TestCase

class LocationTests(TestCase):
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    def setUp(self):
        Location.objects.create(city=LocationTests.CITY,country=LocationTests.COUNTRY)

    def test_text_content(self):
        location = Location.objects.get(id=1)
        expected_object_name = location.city
        self.assertEquals(expected_object_name, LocationTests.CITY)