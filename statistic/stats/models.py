from django.db import models


class BgStat(models.Model):
    """статистика фоновой музыки."""

    client_id = models.PositiveIntegerField(verbose_name="ID")
    hash = models.CharField(max_length=32, verbose_name="Контрольная сумма ролика")
    start_at = models.DateTimeField(verbose_name="Дата и время начала вещания")
    length = models.PositiveIntegerField(verbose_name="Хронометраж")
    file_id = models.PositiveIntegerField(
        verbose_name="ID роилка",
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"{self.pk} {self.client_id} {self.hash} {self.start_at} {self.length}"

    class Meta:
        verbose_name = "Статистика музыки"
        verbose_name_plural = "Статистика музыки"


class AdStat(models.Model):
    """статистика Рекламы."""

    client_id = models.PositiveIntegerField(verbose_name="ID")
    hash = models.CharField(max_length=32, verbose_name="Контрольная сумма ролика")
    start_at = models.DateTimeField(verbose_name="Датаи время начала вещания")
    length = models.PositiveIntegerField(verbose_name="Хронометраж")
    time_block = models.TimeField(verbose_name="блок вещания ролика", null=True)
    file_id = models.PositiveIntegerField(
        verbose_name="ID роилка",
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"{self.pk} {self.client_id} {self.hash} {self.start_at} {self.length}"

    class Meta:
        verbose_name = "Статистика рекламы"
        verbose_name_plural = "Статистика рекламы"


class TwoDaysBgStat(models.Model):
    """статистика фоновой музыки за последние 2 дня."""

    client_id = models.PositiveIntegerField(verbose_name="ID")
    hash = models.CharField(
        max_length=32,
        verbose_name="Контрольная сумма ролика"
    )
    start_at = models.DateTimeField(
        verbose_name="Дата и время начала вещания"
    )
    length = models.PositiveIntegerField(verbose_name="Хронометраж")
    file_id = models.PositiveIntegerField(
        verbose_name="ID роилка",
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"{self.pk} {self.client_id} {self.hash} {self.start_at} {self.length}"

    class Meta:
        verbose_name = "Статистика музыки за 2 дня"
        verbose_name_plural = "Статистика музыки за 2 дня"


class TwoDaysAdStat(models.Model):
    """статистика Рекламы за последние 2 дня."""

    client_id = models.PositiveIntegerField(verbose_name="ID")
    hash = models.CharField(
        max_length=32,
        verbose_name="Контрольная сумма ролика"
    )
    start_at = models.DateTimeField(verbose_name="Датаи время начала вещания")
    length = models.PositiveIntegerField(verbose_name="Хронометраж")
    time_block = models.TimeField(verbose_name="блок вещания ролика", null=True)
    file_id = models.PositiveIntegerField(
        verbose_name="ID роилка",
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"{self.pk} {self.client_id} {self.hash} {self.start_at} {self.length}"

    class Meta:
        verbose_name = "Статистика рекламы за 2 дня"
        verbose_name_plural = "Статистика рекламы за 2 дня"


class HashTable(models.Model):
    """Хэш таблица с количеством выходов ролика в день."""
    is_ad = models.BooleanField(verbose_name="Является рекламой")
    client_id = models.PositiveIntegerField(verbose_name="ID машины")
    hash = models.CharField(
        max_length=32,
        verbose_name="Контрольная сумма ролика"
    )
    date = models.DateField(verbose_name="Дата")
    count = models.PositiveIntegerField(
        verbose_name="Количество выходов за день"
    )

    def __str__(self):
        return f"{self.date} {self.client_id} {self.hash} {self.count}"

    class Meta:
        verbose_name = "Количество выходов"
        verbose_name_plural = "Количество выходов"
