from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from .views import (
    HwInfoViewSet, NetworkConfigViewSet, AudioDeviceViewSet,
    BgStatViewSet, AdStatViewSet,
    AdStatDetailViewSet, BgStatDetailViewSet,
    NomenclatureViewSet, IndividualGraphicViewSet,
    ApiNameViewSet, NomenclatureStatusViewSet,
    NomenclatureStatusHistoryViewSet, TimeZoneViewSet
)

schema_view = get_schema_view(
   openapi.Info(
      title="Statistic API",
      default_version='1.0.0',
      description="Документация для сервиса сбора статистики",
      contact=openapi.Contact(email="borisovi@krasrm.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

hw_router = SimpleRouter()
router = SimpleRouter()
nomenclature_router = SimpleRouter()

nomenclature_router.register(
    'api_name',
    ApiNameViewSet,
    basename='api_name'
)
nomenclature_router.register(
    'graphics',
    IndividualGraphicViewSet,
    'graphics'
)
nomenclature_router.register(
    'detail_ad_stat',
    AdStatDetailViewSet,
    'detail_ad_stat'
)
nomenclature_router.register(
    'detail_bg_stat',
    BgStatDetailViewSet,
    basename='detail_bg_stat'
)
nomenclature_router.register(
    'status_history',
    NomenclatureStatusHistoryViewSet,
    basename='status_history'
)
nomenclature_router.register(
    'time_zone',
    TimeZoneViewSet,
    basename='time_zone'
)
router.register(
    'status',
    NomenclatureStatusViewSet,
    basename='status'
)
router.register('nomenclature', NomenclatureViewSet, basename='nomenclature')
router.register('hw_info', HwInfoViewSet, basename='hw_info')
router.register('networks', NetworkConfigViewSet, basename='networks')
router.register(
    'audio_devices',
    AudioDeviceViewSet,
    basename='audio_devices'
)
router.register('ad_stat', AdStatViewSet, basename='ad_stat')
router.register('bg_stat', BgStatViewSet, basename='bg_stat')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/nomenclature/<int:client_id>/', include(nomenclature_router.urls)),
    path('api/v1/', include(router.urls)),
    path('api/v1/schema', schema_view)
]

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
