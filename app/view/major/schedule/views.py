from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.messages.views import SuccessMessageMixin

from common.timetable.models import Timetable
from .form import *

class ScheduleListView(ListView):
    template_name = 'schedule/list.html'
    context_object_name = 'schedules'
    queryset = Timetable.objects.all()


class ScheduleDetailView(DetailView):
    model = Timetable
    template_name = 'schedule/single.html'
    context_object_name = 'schedule'
    slug_field = "pk"


class ScheduleCreateView(SuccessMessageMixin, CreateView):
    template_name = 'schedule/form.html'
    context_object_name = 'data'
    form_class = ScheduleForm
    success_message = _('Schedule successfully added')
    success_url = reverse_lazy("schedule:list")


class ScheduleUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'schedule/form.html'
    model = Timetable
    form_class = ScheduleForm
    success_message =  _('Schedule successfully updated')
    success_url = reverse_lazy("schedule:list")

    def get_success_url(self):
        return reverse_lazy("schedule:list")

class ScheduleDeleteView(SuccessMessageMixin, DeleteView):
    model = Timetable
    success_url = reverse_lazy("schedule:list")
    success_message =  _('Schedule successfully deleted')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ScheduleDeleteView , self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
