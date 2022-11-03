from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from stats.views import BgViewSet, AdViewSet

router = SimpleRouter()

router.register(r'bg', BgViewSet)
router.register(r'ad', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += router.urls
