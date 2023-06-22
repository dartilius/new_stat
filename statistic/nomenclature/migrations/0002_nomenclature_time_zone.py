# Generated by Django 3.2.16 on 2023-04-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomenclature',
            name='time_zone',
            field=models.CharField(choices=[('Etc/GMT+11', 'UTC-11'), ('Etc/GMT+10', 'UTC-10'), ('Etc/GMT+9', 'UTC-9'), ('Etc/GMT+8', 'UTC-8'), ('Etc/GMT+7', 'UTC-7'), ('Etc/GMT+6', 'UTC-6'), ('Etc/GMT+5', 'UTC-5'), ('Etc/GMT+4', 'UTC-4'), ('Etc/GMT+3', 'UTC-3'), ('Etc/GMT+2', 'UTC-2'), ('Etc/GMT+1', 'UTC-1'), ('Etc/GMT+0', 'UTC'), ('Etc/GMT-1', 'UTC+1'), ('Etc/GMT-2', 'UTC+2'), ('Etc/GMT-3', 'UTC+3'), ('Etc/GMT-4', 'UTC+4'), ('Etc/GMT-5', 'UTC+5'), ('Etc/GMT-6', 'UTC+6'), ('Etc/GMT-7', 'UTC+7'), ('Etc/GMT-8', 'UTC+8'), ('Etc/GMT-9', 'UTC+9'), ('Etc/GMT-10', 'UTC+10'), ('Etc/GMT-11', 'UTC+11'), ('Etc/GMT-12', 'UTC+12')], default='Etc/GMT-7', max_length=100, verbose_name='Часовой пояс'),
        ),
    ]