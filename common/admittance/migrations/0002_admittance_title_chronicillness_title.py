# Generated by Django 4.0.3 on 2022-04-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admittance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admittance',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chronicillness',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
    ]