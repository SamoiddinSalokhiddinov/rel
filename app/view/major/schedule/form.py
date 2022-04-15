from dataclasses import fields
from pydoc import Doc
from traceback import print_tb
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.timetable.models import *

class ScheduleForm(forms.ModelForm):
    error_field = dict(required=_("Please  choose this field" , invalid=_("Enter this field")))
    monday_start = forms.TimeField(
        widget=forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
        error_messages=error_field
    )
    class Meta:
        model = Timetable
        fields = "__all__"
        exclude = ['created_at', 'updated_at', ]
        widgets = {
            "doctor" : forms.Select(attrs={"class": "form-control"}),
            "monday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "tuesday_start" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "tuesday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "wednesday_start" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "wednesday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "thursday_start" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "thursday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "friday_start" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "friday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "saturday_start" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "saturday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "sunday_start" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
            "sunday_end" :  forms.TimeInput(attrs={"class" : "form-control" , "type" : "time" , "required":"true"}),
        }



 