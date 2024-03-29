# Generated by Django 3.2.16 on 2023-06-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0003_nomenclature_time_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomenclature',
            name='avail_interval',
            field=models.PositiveSmallIntegerField(default=1800, verbose_name='Интервал сервисной доступности'),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='client_avail_interval',
            field=models.PositiveSmallIntegerField(default=7200, verbose_name='Интервал клиентской доступности'),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='service_avail_interval',
            field=models.PositiveSmallIntegerField(default=10, verbose_name='Интервал служебной доступности'),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='store_client_history',
            field=models.BooleanField(default=True, verbose_name='Активность истории клиентской доступности'),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='store_history',
            field=models.BooleanField(default=True, verbose_name='Активность истории сервисной доступности'),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='store_service_history',
            field=models.BooleanField(default=False, verbose_name='Активность истории служебной доступности'),
        ),
    ]
