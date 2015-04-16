from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import LocationViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [    
    url(r'^api/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
