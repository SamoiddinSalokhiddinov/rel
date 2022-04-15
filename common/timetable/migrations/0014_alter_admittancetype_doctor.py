# Generated by Django 3.2.12 on 2022-04-06 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20220326_1637'),
        ('timetable', '0013_auto_20220406_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admittancetype',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admittance_type_doctor', to='doctor.doctor', verbose_name='Doctor'),
        ),
    ]
