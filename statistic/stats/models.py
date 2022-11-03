from django.db import models


class BgStat(models.Model):
    """статистика фоновой музыки."""

    client_id = models.PositiveIntegerField(verbose_name="ID")
    hash = models.CharField(max_length=32, verbose_name="Контрольная сумма ролика")
    start_at = models.DateTimeField(verbose_name="Дата и время начала вещания")
    length = models.PositiveIntegerField(verbose_name="Хронометраж")

    def __str__(self):
        return f"{self.pk} {self.hash} {self.client_id} {self.length}"

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

    def __str__(self):
        return f"{self.pk} {self.hash} {self.client_id} {self.length}"

    class Meta:
        verbose_name = "Статистика рекламы"
        verbose_name_plural = "Статистика рекламы"