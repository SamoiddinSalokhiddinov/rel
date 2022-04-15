
from datetime import date , datetime
from tokenize import blank_re
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from common.doctor.models import Doctor
from common.patient.models import Patient
from datetime import datetime, timedelta, time
from ckeditor.fields import RichTextField


class Timetable(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="timetable_doctor")
    
    monday_start = models.TimeField(verbose_name=_("(Monday) Start Hour"), blank=True)
    monday_end = models.TimeField(verbose_name=_("(Monday) End Hour"), blank=True)

    tuesday_start = models.TimeField(verbose_name=_("(Tuesday) Start Hour"), blank=True)
    tuesday_end = models.TimeField(verbose_name=_("(Tuesday) End Hour"), blank=True)

    wednesday_start = models.TimeField(verbose_name=_("(Wednesday) Start Hour"), blank=True)
    wednesday_end = models.TimeField(verbose_name=_("(Wednesday) End Hour"), blank=True)
    
    thursday_start = models.TimeField(verbose_name=_("(Thursday) Start Hour"), blank=True)
    thursday_end = models.TimeField(verbose_name=_("(Thursday) End Hour"), blank=True)

    friday_start = models.TimeField(verbose_name=_("(Friday) Start Hour"), blank=True)
    friday_end = models.TimeField(verbose_name=_("(Friday) End Hour"), blank=True)

    saturday_start = models.TimeField(verbose_name=_("(Saturday) Start Hour"), blank=True)
    saturday_end = models.TimeField(verbose_name=_("(Saturday) End Hour"), blank=True)

    sunday_start = models.TimeField(verbose_name=_("(Sunday) Start Hour"), blank=True)
    sunday_end = models.TimeField(verbose_name=_("(Sunday) End Hour"), blank=True)

    

    class Meta:
        verbose_name = _("Timetable")
        verbose_name_plural = _("Timetables")
