from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from ona.models import Location, LocationType

admin.site.register(Location, MPTTModelAdmin)
admin.site.register(LocationType)
