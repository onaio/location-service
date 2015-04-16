from django.conf.urls import include, url
from django.contrib import admin
from api.urls import router

urlpatterns = [
    # Examples:
    # url(r'^$', 'onalocation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
