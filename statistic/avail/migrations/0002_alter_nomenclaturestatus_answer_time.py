# Generated by Django 3.2.16 on 2023-04-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomenclaturestatus',
            name='answer_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее время ответа'),
        ),
    ]
