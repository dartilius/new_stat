from django.db import models
from nomenclature.models import Nomenclature

STATUSES = (
    (1, 'Доступна'),
    (2, 'Недоступна по графику'),
    (3, 'Недоступна')
)
CLIENT_STATUSES = (
    (1, 'Доступна'),
    (3, 'Недоступна')
)


class NomenclatureStatus(models.Model):
    """Доступность номенклатуры."""

    client = models.ForeignKey(
        Nomenclature,
        primary_key=True,
        unique=True,
        verbose_name='status',
        on_delete=models.CASCADE
    )
    service_status = models.PositiveSmallIntegerField(
        choices=STATUSES,
        verbose_name='Служебная доступность',
        default=1
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUSES,
        verbose_name='Сервисная доступность',
        default=1
    )
    client_status = models.PositiveSmallIntegerField(
        choices=CLIENT_STATUSES,
        verbose_name='Клиентская доступность',
        default=1
    )
    answer_time = models.DateTimeField(
        verbose_name='Последнее время ответа'
    )

    def __str__(self):
        return f'{self.client}: {self.answer_time}'

    class Meta:
        verbose_name = 'Статус доступности'
        verbose_name_plural = 'Статусы доступности'


class NomenclatureStatusHistory(models.Model):
    """История изменения статусов сервисной доступности."""

    client = models.ForeignKey(
        Nomenclature,
        verbose_name='ID',
        related_name='history',
        on_delete=models.CASCADE
    )
    to_status = models.PositiveSmallIntegerField(
        choices=STATUSES,
        verbose_name='Статус после изменеения'
    )
    change_time = models.DateTimeField(
        verbose_name='Время изменеения статуса',
        auto_now_add=True
    )

    def __str__(self):
        return (
            f'{self.client}: статус изменился '
            f'на {self.to_status} в {self.change_time}'
        )

    class Meta:
        verbose_name = 'История статуса'
        verbose_name_plural = 'История статусов'


class Parameters(models.Model):
    """Параметры сервиса."""

    time_delta_available = models.PositiveSmallIntegerField(
        verbose_name='Период доступности секунд'
    )
