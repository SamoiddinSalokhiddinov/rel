from dataclasses import fields
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from common.doctor.models import *
from common.admittance.models import *
class DateInput(forms.DateInput):
    input_type = 'date'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        widgets = {
            "card_id": forms.NumberInput(attrs={"class": "form-control", "placeholder" : _("Enter Card ID ")},),
            "name": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Name ")}),
            "middle_name": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Middle Name ")}), 
            "surname": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Surname ")}),
            "birthday": DateInput(format=('%Y-%m-%d'), attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control" , "placeholder" : _("Enter Email ")}),
            "phone": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Phone ")}), 
            "phone2": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter Phone 2 ")}),
            "hospital": forms.Select(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
            "speciality": forms.Select(attrs={"class": "form-control"}),
            "post": forms.Select(attrs={"class": "form-control"}),
            "city": forms.Select(attrs={"class": "form-control"}),
            "district": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "room": forms.Select(attrs={"class": "form-control"}),
            "floor": forms.Select(attrs={"class": "form-control"}),
        }

    def clean(self):
        cd = self.cleaned_data

        self_id = self.instance.id
        card_id = cd.get("card_id")
        check_cardId = Doctor.objects.filter(card_id=card_id).exists()
        check_doctor = Doctor.objects.filter(id=self_id).exists()

        email = cd.get("email")
        check_email = Doctor.objects.filter(email=email).exists()
        
        if check_cardId and not check_doctor:
            self.add_error("card_id" , _("Card id exists"))
        
        if check_email and not check_doctor:
            self.add_error("email", _("Email exists . Please enter another email"))


        return cd

class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptoms
        fields = "__all__"
        exclude = ['created_at', 'updated_at', ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter title ")}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['doctor'].required = False


class AdmittanceForm(forms.ModelForm):
    class Meta:
        model = Admittance
        fields = "__all__"
        exclude = ['created_at', 'updated_at', 'symptoms', 'diagnosis', 'extra_file' ,]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control" , "placeholder" : _("Enter title ")}),
            "date" : DateInput(format=('%Y-%m-%d'), attrs={"class": "form-control"}),
            "start_hour": forms.TimeInput(attrs={"class" : "form-control" , "type" : "time"}),
            "end_hour": forms.TimeInput(attrs={"class" : "form-control" , "type" : "time"}),
            "doctor" : forms.TextInput(attrs={"class": "form-control d-none",}),
            "status" : forms.Select(attrs={"class": "form-control"} ),
            "patient" : forms.Select(attrs={"class": "select2 form-select patient_select" ,}),
            "admittance_type" : forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
            
    # def __init__(self,pk , *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     doc = Doctor.objects.filter(id=pk)
    #     print("doctr" ,doc)
    #     self.fields["doctor"].queryset = doc

