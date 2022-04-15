from dataclasses import fields
from django.contrib import admin
from .models import *
from datetime import datetime , time
from django.utils.translation import gettext_lazy as _



admin.site.register(Admittance) 
admin.site.register(AdmittanceType) 
admin.site.register(ChronicIllness) 
admin.site.register(Symptoms) 