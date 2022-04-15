# Generated by Django 4.0.3 on 2022-04-13 10:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0005_doctor_floor_doctor_room'),
        ('patient', '0004_alter_patient_card_id_alter_patient_middle_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmittanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('color', models.CharField(choices=[('#0d6efd', 'primary'), ('#dc3545', 'danger'), ('#6c757d', 'secondary'), ('#198754', 'success'), ('#ffc107', 'warning'), ('#f8f9fa', 'light'), ('#212529', 'dark')], default=(('#0d6efd', 'primary'), ('#dc3545', 'danger'), ('#6c757d', 'secondary'), ('#198754', 'success'), ('#ffc107', 'warning'), ('#f8f9fa', 'light'), ('#212529', 'dark')), max_length=100, verbose_name='Colors')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated_at')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_type_doctor', to='doctor.doctor', verbose_name='Doctor')),
            ],
            options={
                'verbose_name': 'Admittance Type',
                'verbose_name_plural': 'Admittance Types',
            },
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated_at')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='symp_doctor', to='doctor.doctor', verbose_name='Doctor')),
            ],
            options={
                'verbose_name': 'Symptoms',
                'verbose_name_plural': 'Symptoms',
            },
        ),
        migrations.CreateModel(
            name='ChronicIllness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Date')),
                ('start_hour', models.TimeField(blank=True, verbose_name='Start Hour')),
                ('end_hour', models.TimeField(blank=True, verbose_name='End Hour')),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('admitting', 'Admitting'), ('admitted', 'Admitted')], default=('waiting', 'Waiting'), max_length=100, verbose_name='Status')),
                ('diagnosis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated_at')),
                ('extra_file', models.FileField(blank=True, null=True, upload_to='doctors/', verbose_name='Extra file')),
                ('admittance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ill_its_type', to='admittance.admittancetype', verbose_name='Admittance Type')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ill_doctor', to='doctor.doctor', verbose_name='Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ill_patient', to='patient.patient', verbose_name='Patient')),
                ('symptoms', models.ManyToManyField(blank=True, to='admittance.symptoms', verbose_name='Symptoms')),
            ],
            options={
                'verbose_name': 'Admittance',
                'verbose_name_plural': 'Admittances',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Admittance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Date')),
                ('start_hour', models.TimeField(blank=True, verbose_name='Start Hour')),
                ('end_hour', models.TimeField(blank=True, verbose_name='End Hour')),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('admitting', 'Admitting'), ('admitted', 'Admitted')], default=('waiting', 'Waiting'), max_length=100, verbose_name='Status')),
                ('diagnosis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated_at')),
                ('extra_file', models.FileField(blank=True, null=True, upload_to='doctors/', verbose_name='Extra file')),
                ('admittance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_its_type', to='admittance.admittancetype', verbose_name='Admittance Type')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_doctor', to='doctor.doctor', verbose_name='Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_patient', to='patient.patient', verbose_name='Patient')),
                ('symptoms', models.ManyToManyField(blank=True, to='admittance.symptoms', verbose_name='Symptoms')),
            ],
            options={
                'verbose_name': 'Admittance',
                'verbose_name_plural': 'Admittances',
                'ordering': ['-id'],
            },
        ),
    ]