from django.db import models
from jsonfield import JSONField
from mptt.models import MPTTModel, TreeForeignKey


class LocationType(models.Model):
    name = models.CharField(max_length=200)


class Location(MPTTModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True)
    metadata = JSONField(blank=True)
    location_type = models.ForeignKey(LocationType)
