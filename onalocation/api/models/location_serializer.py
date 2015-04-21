from rest_framework import serializers

from ona.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    location_type = serializers.CharField(max_length=200)
    children = serializers.SerializerMethodField('get_children_map')

    class Meta:
        model = Location
        fields = ('name', 'code', 'children', 'metadata', 'location_type')

    def get_children_map(self, obj):
        if obj:
            children = [{'id': c.id,
                        'name': c.name,
                        'code': c.code,
                        'meta': c.metadata} for c in obj.children.all()]

            return children
