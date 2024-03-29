# Generated by Django 3.2.16 on 2023-06-07 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0004_auto_20230607_0948'),
        ('avail', '0003_alter_nomenclaturestatus_answer_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomenclaturestatus',
            name='client_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Доступна'), (3, 'Недоступна')], default=1, verbose_name='Клиентская доступность'),
        ),
        migrations.AddField(
            model_name='nomenclaturestatus',
            name='service_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Доступна'), (2, 'Недоступна по графику'), (3, 'Недоступна')], default=1, verbose_name='Служебная доступность'),
        ),
        migrations.AlterField(
            model_name='nomenclaturestatus',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Доступна'), (2, 'Недоступна по графику'), (3, 'Недоступна')], default=1, verbose_name='Сервисная доступность'),
        ),
        migrations.CreateModel(
            name='ServiceStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_status', models.PositiveSmallIntegerField(choices=[(1, 'Доступна'), (2, 'Недоступна по графику'), (3, 'Недоступна')], verbose_name='Статус после изменеения')),
                ('change_time', models.DateTimeField(auto_now_add=True, verbose_name='Время изменеения статуса')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_history', to='nomenclature.nomenclature', verbose_name='ID')),
            ],
            options={
                'verbose_name': 'История служебного статуса',
                'verbose_name_plural': 'История служебных статусов',
            },
        ),
        migrations.CreateModel(
            name='ClientStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_status', models.PositiveSmallIntegerField(choices=[(1, 'Доступна'), (2, 'Недоступна по графику'), (3, 'Недоступна')], verbose_name='Статус после изменеения')),
                ('change_time', models.DateTimeField(auto_now_add=True, verbose_name='Время изменеения статуса')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_history', to='nomenclature.nomenclature', verbose_name='ID')),
            ],
            options={
                'verbose_name': 'История статуса',
                'verbose_name_plural': 'История статусов',
            },
        ),
    ]
