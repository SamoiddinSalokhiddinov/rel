# Generated by Django 4.0.3 on 2022-04-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0028_admittance_diagnosis_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admittance',
            old_name='diagnosis_file',
            new_name='extra_file',
        ),
    ]