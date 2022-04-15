
from datetime import date , datetime
from statistics import mode
from tokenize import blank_re
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from common.doctor.models import Doctor
from common.patient.models import Patient
from datetime import datetime, timedelta, time
from ckeditor.fields import RichTextField

COLORS = (
    ( "#0d6efd", "primary"),
    ( "#dc3545", "danger"),
    ( "#6c757d", "secondary"),
    ( "#198754", "success"),
    ( "#ffc107", "warning"),
    ( "#f8f9fa", "light"),
    ( "#212529", "dark"),
)

STATUS = (
    ( "waiting", _("Waiting")),
    ( "admitting", _("Admitting")),
    ( "admitted", _("Admitted")),
)
GENDER = (
    (1, _("Male")),
    (2, _("Female"))
)

class AdmittanceType(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="ad_type_doctor")
    title = models.CharField(_("Title"), max_length=100)
    color = models.CharField(choices=COLORS, verbose_name=_("Colors"), default=COLORS, max_length=100)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)

    def __str__(self):
            return self.title

    @property
    def color_class(self):
        return self.get_color_display

    class Meta:
        verbose_name = _("Admittance Type")
        verbose_name_plural = _("Admittance Types")



class Symptoms(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="symp_doctor")
    title = models.CharField(_("Title"), max_length=100)

    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = _("Symptoms")
        verbose_name_plural = _("Symptoms")



class ChronicIllness(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    date = models.DateField(_("Date"), null=True)
    start_hour = models.TimeField(verbose_name=_("Start Hour"),blank=True,)
    end_hour = models.TimeField(verbose_name=_("End Hour"),blank=True,)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="ill_doctor")
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name="ill_patient",)
    admittance_type = models.ForeignKey(AdmittanceType, verbose_name=_("Admittance Type"), on_delete=models.CASCADE, related_name="ill_its_type")
    status = models.CharField(choices=STATUS, verbose_name=_("Status"), default=STATUS[0], max_length=100)
    symptoms = models.ManyToManyField(Symptoms, verbose_name=_("Symptoms"),  blank=True)
    diagnosis = RichTextField(blank=True,null=True)
    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)
    extra_file = models.FileField(_("Extra file"), upload_to="doctors/", null=True , blank=True)

    def __str__(self):
        return "Dr " + self.doctor.surname + " : " + "Patient " + self.patient.surname + " Hour : " + str(self.start_hour )

    @property
    def work_hour(self):
        end_hour = datetime.combine(datetime.now(), self.end_hour)
        start_hour = datetime.combine(datetime.now(), self.start_hour)
        diff = end_hour - start_hour
        return diff

    def get_today_patient(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        print(self.filter(start__lte=today_end, end__gte=today_start))
        return self.filter(start__lte=today_end, end__gte=today_start)
    class Meta:
        ordering = ['-id']  
        verbose_name = _("Chronic illnes")
        verbose_name_plural = _("Chronic illnes")


class Admittance(models.Model):
    date = models.DateField(_("Date"), null=True)
    title = models.CharField(_("Title"), max_length=100)
    start_hour = models.TimeField(verbose_name=_("Start Hour"),blank=True,)
    end_hour = models.TimeField(verbose_name=_("End Hour"),blank=True,)
    doctor = models.ForeignKey(Doctor, verbose_name=_("Doctor"), on_delete=models.CASCADE, related_name="ad_doctor")
    patient = models.ForeignKey(Patient, verbose_name=_("Patient"), on_delete=models.CASCADE, related_name="ad_patient",)
    admittance_type = models.ForeignKey(AdmittanceType, verbose_name=_("Admittance Type"), on_delete=models.CASCADE, related_name="ad_its_type")
    status = models.CharField(choices=STATUS, verbose_name=_("Status"), default=STATUS[0], max_length=100)
    symptoms = models.ManyToManyField(Symptoms, verbose_name=_("Symptoms"),  blank=True)
    diagnosis = RichTextField(blank=True,null=True)
    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated_at"), default=timezone.now)
    extra_file = models.FileField(_("Extra file"), upload_to="doctors/", null=True , blank=True)

    def __str__(self):
        return "Dr " + self.doctor.surname + " : " + "Patient " + self.patient.surname + " Hour : " + str(self.start_hour )

    @property
    def work_hour(self):
        end_hour = datetime.combine(datetime.now(), self.end_hour)
        start_hour = datetime.combine(datetime.now(), self.start_hour)
        diff = end_hour - start_hour
        return diff

    def get_today_patient(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        print(self.filter(start__lte=today_end, end__gte=today_start))
        return self.filter(start__lte=today_end, end__gte=today_start)
    class Meta:
        ordering = ['-id']  
        verbose_name = _("Admittance")
        verbose_name_plural = _("Admittances")

   