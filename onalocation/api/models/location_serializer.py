from rest_framework import serializers

from ona.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    location_type = serializers.CharField(max_length=200)

    class Meta:
        model = Location
        fields = ('name', 'code', 'children', 'metadata', 'location_type')
