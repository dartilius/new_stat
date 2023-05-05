from django.db import models
from nomenclature.models import Nomenclature


class HwInfo(models.Model):
    """Информация об оборудовании."""
    client = models.ForeignKey(
        Nomenclature,
        verbose_name='ID',
        primary_key=True,
        unique=True,
        on_delete=models.CASCADE
    )
    city = models.CharField(
        max_length=511,
        verbose_name='Город',
        null=True,
        blank=True
    )
    model = models.CharField(
        max_length=511,
        verbose_name='Модель',
        null=True,
        blank=True
    )
    provider = models.CharField(
        max_length=511,
        verbose_name='Провайдер',
        null=True,
        blank=True
    )
    ext_ip = models.CharField(
        max_length=63,
        verbose_name='Внешний IP',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Информация об оборудовании'
        verbose_name_plural = 'Информация об оборудовании'


class NetworkConfig(models.Model):
    """Интернет конфигурация."""
    hw_info = models.ForeignKey(
        HwInfo,
        verbose_name='hw_info_id',
        related_name='networks',
        on_delete=models.CASCADE,
    )
    interface = models.CharField(max_length=511, verbose_name='Интерфейс')
    mac = models.CharField(max_length=63, verbose_name='Мак адресс')
    ip = models.CharField(max_length=63, verbose_name='IP адресс')

    def __str__(self):
        return f'{self.hw_info} {self.interface} {self.ip} {self.mac}'

    class Meta:
        verbose_name = 'Интернет конфигурация'
        verbose_name_plural = 'Интернет конфигурация'


class AudioDevice(models.Model):
    """Звуковые карты."""
    hw_info = models.ForeignKey(
        HwInfo,
        verbose_name='hw_info_id',
        related_name='audio_devices',
        on_delete=models.CASCADE
    )
    device_id = models.PositiveSmallIntegerField(
        verbose_name='Номер карты'
    )
    device_name = models.CharField(max_length=511, verbose_name='Имя карты')
    device_item = models.CharField(
        max_length=63,
        verbose_name='Имя регулировки',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.hw_info} {self.device_name}'

    class Meta:
        verbose_name = 'Звуковая карта'
        verbose_name_plural = 'Звуковые карты'
