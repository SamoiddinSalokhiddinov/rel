# Generated by Django 4.0.3 on 2022-04-11 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0029_rename_diagnosis_file_admittance_extra_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admittance',
            name='extra_file',
            field=models.FileField(blank=True, null=True, upload_to='doctors/', verbose_name='Extra file'),
        ),
    ]
