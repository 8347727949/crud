from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class subjectForm(forms.ModelForm):
    class Meta:
        model = subjectdetail
        fields="__all__"

class HotelForm(forms.ModelForm):  
    class Meta:  
        model = Hotel
        fields = "__all__" 

class ProgramForm(forms.ModelForm):  
    class Meta:  
        model = Programmes
        fields = ['program_code','prog_name','prog_duration'] 

class SemestersForm(forms.ModelForm):  
    class Meta:  
        model = Semesters 
        fields = "__all__"  

class CourceForm(forms.ModelForm):  
    class Meta:  
        model = Cource
        fields = "__all__"  

class Request_provisional_Form(forms.ModelForm):  
    class Meta:  
        model = Request_provisional
        fields = "__all__" 

class Request_final_result_Form(forms.ModelForm):  
    class Meta:  
        model = Request_final_result
        fields = "__all__"  

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]