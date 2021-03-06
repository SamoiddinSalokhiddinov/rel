# Generated by Django 3.2.12 on 2022-03-28 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20220326_1637'),
        ('timetable', '0004_remove_schedule_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedure_type_doctor', to='doctor.doctor', verbose_name='Doctor')),
            ],
        ),
    ]
