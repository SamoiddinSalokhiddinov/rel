# Generated by Django 4.0.3 on 2022-04-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0017_alter_admittancetype_color_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admittancetype',
            name='color_class',
            field=models.CharField(choices=[('#0d6efd', 'primary'), ('#dc3545', 'danger'), ('#6c757d', 'secondary'), ('#198754', 'success'), ('#ffc107', 'warning'), ('#f8f9fa', 'light'), ('#212529', 'dark')], default=1, max_length=100, verbose_name='Colors'),
        ),
    ]
