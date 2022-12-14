# Generated by Django 4.1.3 on 2022-11-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_alter_adstat_options_alter_bgstat_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adstat',
            name='time_block',
            field=models.TimeField(null=True, verbose_name='блок вещания ролика'),
        ),
        migrations.AlterField(
            model_name='adstat',
            name='client_id',
            field=models.PositiveIntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='adstat',
            name='hash',
            field=models.CharField(max_length=32, verbose_name='Контрольная сумма ролика'),
        ),
        migrations.AlterField(
            model_name='adstat',
            name='length',
            field=models.PositiveIntegerField(verbose_name='Хронометраж'),
        ),
        migrations.AlterField(
            model_name='adstat',
            name='start_at',
            field=models.DateTimeField(verbose_name='Датаи время начала вещания'),
        ),
        migrations.AlterField(
            model_name='bgstat',
            name='hash',
            field=models.CharField(max_length=32, verbose_name='Контрольная сумма ролика'),
        ),
        migrations.AlterField(
            model_name='bgstat',
            name='length',
            field=models.PositiveIntegerField(verbose_name='Хронометраж'),
        ),
        migrations.AlterField(
            model_name='bgstat',
            name='start_at',
            field=models.DateTimeField(verbose_name='Дата и время начала вещания'),
        ),
    ]
