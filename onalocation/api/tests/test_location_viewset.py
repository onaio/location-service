from api.tests import TestAbstractViewSet
from api.viewsets import LocationViewSet


class TestLocationViewSet(TestAbstractViewSet):
    def setUp(self):
        super(TestLocationViewSet, self).setUp()
        self.view = LocationViewSet.as_view({
            "get": "list"})
        self.state = self._create_location(name="Distrito Federal",
                                           code="abcde",
                                           location_type="State")
        self.municipality = self._create_location(name="Guara",
                                                  code="12345",
                                                  location_type="Municipality",
                                                  parent=self.state.name)
        self.clinic = self._create_location(name="Clinic Guara",
                                            code="23456789",
                                            location_type="Clinic",
                                            parent=self.municipality)

    def test_get_all_locations(self):
        request = self.factory.get('/')

        response = self.view(request)
        self.assertEqual(response.status_code, 200)

        state = response.data[0]
        self.assertEqual(state['name'], "Distrito Federal")
        self.assertEqual(len(response.data), 3)

    def test_location_data_by_id(self):
        request = self.factory.get('/{}'.format(self.state.id))

        response = self.view(request)
        self.assertEqual(response.status_code, 200)

        state = response.data[0]
        self.assertEqual(state['name'], "Distrito Federal")
        self.assertEqual(len(state['children']), 1)
