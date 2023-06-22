from django.db import models

TIMEZONES = [
    ('Etc/GMT+11', "UTC-11"),
    ('Etc/GMT+10', "UTC-10"),
    ('Etc/GMT+9', "UTC-9"),
    ('Etc/GMT+8', "UTC-8"),
    ('Etc/GMT+7', "UTC-7"),
    ('Etc/GMT+6', "UTC-6"),
    ('Etc/GMT+5', "UTC-5"),
    ('Etc/GMT+4', "UTC-4"),
    ('Etc/GMT+3', "UTC-3"),
    ('Etc/GMT+2', "UTC-2"),
    ('Etc/GMT+1', "UTC-1"),
    ('Etc/GMT+0', "UTC"),
    ('Etc/GMT-1', "UTC+1"),
    ('Etc/GMT-2', "UTC+2"),
    ('Etc/GMT-3', "UTC+3"),
    ('Etc/GMT-4', "UTC+4"),
    ('Etc/GMT-5', "UTC+5"),
    ('Etc/GMT-6', "UTC+6"),
    ('Etc/GMT-7', "UTC+7"),
    ('Etc/GMT-8', "UTC+8"),
    ('Etc/GMT-9', "UTC+9"),
    ('Etc/GMT-10', "UTC+10"),
    ('Etc/GMT-11', "UTC+11"),
    ('Etc/GMT-12', "UTC+12")
]


class Nomenclature(models.Model):
    """Номенклатура."""

    client_id = models.PositiveIntegerField(
        verbose_name="ID",
        primary_key=True,
    )
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    name = models.CharField(max_length=511, verbose_name='Название')
    mon_start_time = models.TimeField(verbose_name='Время начала ПН')
    mon_end_time = models.TimeField(verbose_name='Время окончания ПН')
    tue_start_time = models.TimeField(verbose_name='Время начала ВТ')
    tue_end_time = models.TimeField(verbose_name='Время окончания ВТ')
    wed_start_time = models.TimeField(verbose_name='Время начала СР')
    wed_end_time = models.TimeField(verbose_name='Время окончания СР')
    thu_start_time = models.TimeField(verbose_name='Время начала ЧТ')
    thu_end_time = models.TimeField(verbose_name='Время окончания ЧТ')
    fri_start_time = models.TimeField(verbose_name='Время начала ПТ')
    fri_end_time = models.TimeField(verbose_name='Время окончания ПТ')
    sat_start_time = models.TimeField(verbose_name='Время начала СБ')
    sat_end_time = models.TimeField(verbose_name='Время окончания СБ')
    sun_start_time = models.TimeField(verbose_name='Время начала ВС')
    sun_end_time = models.TimeField(verbose_name='Время окончания ВС')
    service_avail_interval = models.PositiveSmallIntegerField(
        verbose_name='Интервал служебной доступности',
        default=10
    )
    avail_interval = models.PositiveSmallIntegerField(
        verbose_name='Интервал сервисной доступности',
        default=1800
    )
    client_avail_interval = models.PositiveSmallIntegerField(
        verbose_name='Интервал клиентской доступности',
        default=7200
    )
    store_service_history = models.BooleanField(
        verbose_name='Активность истории служебной доступности',
        default=False
    )
    store_history = models.BooleanField(
        verbose_name='Активность истории сервисной доступности',
        default=True
    )
    store_client_history = models.BooleanField(
        verbose_name='Активность истории клиентской доступности',
        default=True
    )
    time_zone = models.CharField(
        max_length=100,
        choices=TIMEZONES,
        default='Etc/GMT-7',
        verbose_name='Часовой пояс'
    )

    def __str__(self):
        return f'{self.client_id}'

    class Meta:
        verbose_name = "Номенклатура"
        verbose_name_plural = "Номенклатуры"


class IndividualGraphic(models.Model):
    """Индивидуальные графики режима вещания."""

    client = models.ForeignKey(
        Nomenclature,
        on_delete=models.CASCADE,
        unique=False,
        verbose_name='ID',
        related_name='graphics'
    )
    start_time = models.TimeField(verbose_name='Время начала')
    end_time = models.TimeField(verbose_name='Время окончания')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f"{self.client} {self.date}: {self.start_time} - {self.end_time}"

    class Meta:
        verbose_name = "Индивидуальный график"
        verbose_name_plural = "Индивидуальные графики"


class ApiName(models.Model):
    """Api имя рабочей станции."""

    client = models.ForeignKey(
        Nomenclature,
        verbose_name='ID',
        primary_key=True,
        unique=True,
        related_name='api_names',
        on_delete=models.CASCADE
    )
    last_answer_time_date = models.DateTimeField(
        verbose_name='Последнее время ответа в API',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=511, verbose_name='Имя в API')

    def __str__(self):
        return f'{self.client}: {self.name} {self.last_answer_time_date}'

    class Meta:
        verbose_name = 'API имя'
        verbose_name_plural = 'API имена'
