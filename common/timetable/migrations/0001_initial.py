# Generated by Django 3.2.12 on 2022-03-28 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0004_auto_20220326_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Date')),
                ('start_hour', models.TimeField(auto_now=True, verbose_name='Start Hour')),
                ('end_hour', models.TimeField(auto_now=True, verbose_name='End Hour')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_doctor', to='doctor.doctor', verbose_name='Doctor')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
    ]
