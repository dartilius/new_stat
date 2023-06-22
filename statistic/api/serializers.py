from rest_framework import serializers
from stats.models import AdStat, BgStat, TwoDaysBgStat, TwoDaysAdStat
from nomenclature.models import Nomenclature, IndividualGraphic, ApiName
from harvest.models import HwInfo, NetworkConfig, AudioDevice
from avail.models import NomenclatureStatus, NomenclatureStatusHistory


class BgStatSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели BgStat."""

    class Meta:
        model = BgStat
        fields = ('client_id', 'hash', 'start_at', 'length', 'file_id')

    def create(self, validated_data):
        TwoDaysBgStat.objects.create(**validated_data)
        return BgStat.objects.create(**validated_data)


class AdStatSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели AdStat."""

    class Meta:
        model = AdStat
        fields = ('client_id', 'hash', 'start_at', 'length', 'time_block', 'file_id')

    def create(self, validated_data):
        TwoDaysAdStat.objects.create(**validated_data)
        return AdStat.objects.create(**validated_data)


class NomenclatureSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Nomenclature."""

    class Meta:
        model = Nomenclature
        fields = (
            'client_id',
            'name',
            'time_zone',
            'is_active',
            'mon_start_time',
            'mon_end_time',
            'tue_start_time',
            'tue_end_time',
            'wed_start_time',
            'wed_end_time',
            'thu_start_time',
            'thu_end_time',
            'fri_start_time',
            'fri_end_time',
            'sat_start_time',
            'sat_end_time',
            'sun_start_time',
            'sun_end_time'
        )


class IndividualGraphicSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели IndividualGraphic"""

    class Meta:
        model = IndividualGraphic
        fields = ('client', 'start_time', 'end_time', 'date')


class ApiNameSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели ApiName."""

    class Meta:
        model = ApiName
        fields = ('client', 'name', 'last_answer_time_date')


class HwInfoSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели HwInfo."""

    class Meta:
        model = HwInfo
        fields = ('client', 'city', 'model', 'provider', 'ext_ip')


class NetworkConfigSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели NetworkConfig."""

    class Meta:
        model = NetworkConfig
        fields = ('hw_info', 'interface', 'mac', 'ip')


class AudioDeviceSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели AudioDevice."""

    class Meta:
        model = AudioDevice
        fields = ('hw_info', 'device_name', 'device_id', 'device_name')


class NomenclatureStatusSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели NomenclatureStatus."""

    class Meta:
        model = NomenclatureStatus
        fields = ('client', 'service_status', 'status', 'client_status', 'answer_time')
        read_only_fields = ('answer_time',)
 
    def validate(self, attrs):
        """Валидация статуса доступности, сохранение истории."""
        client_id = attrs['client']
        nomenclature = Nomenclature.objects.get(client_id=client_id)
        status = NomenclatureStatus.objects.get(client=nomenclature)
        if status.status != 1:
            NomenclatureStatusHistory.objects.create(
                client=nomenclature,
                to_status=1
            )
        return attrs


class NomenclatureStatusHistorySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели NomenclatureStatusHistory."""

    class Meta:
        model = NomenclatureStatusHistory
        fields = ('client', 'to_status', 'change_time')


class TimeZoneSerializer(serializers.ModelSerializer):
    """Сериалайзер для выдачи часовых поясов."""

    class Meta:
        model = Nomenclature
        fields = ('client_id', 'time_zone')
        read_only_fields = fields
