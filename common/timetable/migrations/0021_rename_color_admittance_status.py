# Generated by Django 4.0.3 on 2022-04-09 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0020_admittance_color_alter_admittancetype_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admittance',
            old_name='color',
            new_name='status',
        ),
    ]
