from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ona.models import (
    Location,
    LocationType)


class TestAbstractViewSet(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.factory = APIRequestFactory()

    def _create_location(self, name="test", code="1234", location_type="base",
                         parent=None):
        location_type_obj, created = LocationType.objects.get_or_create(
            name=location_type)
        location_obj, created = Location.objects.get_or_create(
            name=name, code=code, location_type=location_type_obj)

        if parent:
            location_parent, created = Location.objects.get_or_create(
                name=parent)
            location_obj.parent = location_parent
            location_obj.save()

        return location_obj
