# Generated by Django 4.0.3 on 2022-04-13 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0030_alter_admittance_extra_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admittancetype',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='symptoms',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Admittance',
        ),
        migrations.DeleteModel(
            name='AdmittanceType',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='Symptoms',
        ),
    ]
