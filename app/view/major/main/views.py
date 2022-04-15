from django.shortcuts import render
from django.views.generic import ListView, DetailView

from common.doctor.models import Doctor
from common.admittance.models import *
from common.patient.models import *
from common.reception.models import *
from common.nurse.models import *
from common.staff.models import *
# Create your views here.

class MainView(ListView):
    template_name = 'major/index.html'
    context_object_name = 'main_list'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ac_count = Admittance.objects.all().count()
        dr_count = Doctor.objects.all().count()
        pt_count = Patient.objects.all().count()
        rc_count = Receptionist.objects.all().count()
        ns_count = Nurse.objects.all().count()
        st_count = Staff.objects.all().count()
        
        context['ac_count'] = ac_count
        context['dr_count'] = dr_count
        context['pt_count'] = pt_count
        context['rc_count'] = rc_count
        context['ns_count'] = ns_count
        context['st_count'] = st_count

        return context
