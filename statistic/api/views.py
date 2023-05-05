from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.response import Response

from .viewsets import WithoutDestroyViewSet
from .serializers import (
    BgStatSerializer, AdStatSerializer,
    NomenclatureStatusSerializer, NomenclatureSerializer,
    IndividualGraphicSerializer, ApiNameSerializer,
    HwInfoSerializer, NetworkConfigSerializer,
    AudioDeviceSerializer, NomenclatureStatusHistorySerializer, TimeZoneSerializer
)
from avail.models import NomenclatureStatus, NomenclatureStatusHistory
from harvest.models import HwInfo
from nomenclature.models import Nomenclature, ApiName
from stats.models import AdStat, BgStat


class HwInfoViewSet(WithoutDestroyViewSet):
    """Управление записями модели HwInfo."""

    queryset = HwInfo.objects.all()
    serializer_class = HwInfoSerializer


class NetworkConfigViewSet(WithoutDestroyViewSet):
    """Управление записями NetworkConfig."""

    serializer_class = NetworkConfigSerializer

    def get_queryset(self):
        hw_info_id = self.kwargs.get('hw_info_id')
        hw_info = get_object_or_404(HwInfo, pk=hw_info_id)
        queryset = hw_info.networks.all()
        return queryset

    def perform_create(self, serializer):
        hw_info_id = self.kwargs.get('hw_info_id')
        hw_info = get_object_or_404(HwInfo, pk=hw_info_id)
        serializer.save(hw_info=hw_info)


class AudioDeviceViewSet(WithoutDestroyViewSet):
    """Управление записями модели AudioDevice."""

    serializer_class = AudioDeviceSerializer

    def get_queryset(self):
        hw_info_id = self.kwargs.get('hw_info_id')
        hw_info = get_object_or_404(HwInfo, pk=hw_info_id)
        queryset = hw_info.audio_devices.all()
        return queryset


class BgStatViewSet(WithoutDestroyViewSet):
    """Управление записями модели BgStat."""

    queryset = BgStat.objects.all()
    serializer_class = BgStatSerializer
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('=client_id', '=hash', '=time_block')

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)


class AdStatViewSet(WithoutDestroyViewSet):
    """Управление записями модели BgStat."""

    queryset = AdStat.objects.all()
    serializer_class = AdStatSerializer

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)


class NomenclatureViewSet(viewsets.ModelViewSet):
    """Управление записями модели Nomenclature."""

    queryset = Nomenclature.objects.all()
    serializer_class = NomenclatureSerializer

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)


class IndividualGraphicViewSet(viewsets.ModelViewSet):
    """Управление записями модели IndividualGraphic."""

    serializer_class = IndividualGraphicSerializer

    def get_queryset(self):
        nomenclature_id = self.kwargs.get('client_id')
        nomenclature = get_object_or_404(Nomenclature, client=nomenclature_id)
        queryset = nomenclature.graphics.all()
        return queryset

    def perform_create(self, serializer):
        nomenclature_id = self.kwargs.get('id')
        nomenclature = get_object_or_404(Nomenclature, client=nomenclature_id)
        serializer.save(client=nomenclature)


class ApiNameViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Получение записей модели ApiName"""

    queryset = ApiName.objects.all()
    serializer_class = ApiNameSerializer


class BgStatDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение фоновой статистики номенклатуры."""

    serializer_class = BgStatSerializer

    def get_queryset(self):
        nomenclature_id = self.kwargs.get('client_id')
        queryset = BgStat.objects.filter(client_id=nomenclature_id)
        return queryset


class AdStatDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение статистики рекламы номенклатуры."""

    queryset = NomenclatureStatus.objects.all()
    serializer_class = AdStatSerializer


class NomenclatureStatusViewSet(WithoutDestroyViewSet):
    """Статусы доступности номенклатуры."""

    queryset = NomenclatureStatus.objects.all()
    serializer_class = NomenclatureStatusSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        client_id = request.data['client']
        nomenclature = get_object_or_404(Nomenclature, client_id=client_id)
        try:
            NomenclatureStatus.objects.create(client=nomenclature, status=1)
            return Response(status=201)
        except Exception:
            instance = NomenclatureStatus.objects.get(client=nomenclature)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)

    def perform_create(self, serializer):
        client_id = self.request.data['client']
        nomenclature = get_object_or_404(Nomenclature, client_id=client_id)
        serializer.save(client=nomenclature, status=1)

    def perform_update(self, serializer):
        client_id = self.request.data['client']
        nomenclature = Nomenclature.objects.get(client_id=client_id)
        serializer.save(client=nomenclature, status=1)


class NomenclatureStatusHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """История статусов доступности."""

    serializer_class = NomenclatureStatusHistorySerializer

    def get_queryset(self):
        client_id = self.kwargs.get('client_id')
        nomenclature = get_object_or_404(Nomenclature, client_id=client_id)
        return nomenclature.history.all()


class TimeZoneViewSet(viewsets.ReadOnlyModelViewSet):
    """Выдача часовых поясов локальным машинам."""

    serializer_class = TimeZoneSerializer

    def get_queryset(self):
        client_id = self.kwargs.get('client_id')
        nomenclature = get_object_or_404(Nomenclature, client_id=client_id)
        return nomenclature
