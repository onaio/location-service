from rest_framework import viewsets
from api.models import LocationSerializer
from ona.models import Location


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
