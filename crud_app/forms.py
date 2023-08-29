from django import forms
from crud_app.models import projectdetail

class ProgramForm(forms.ModelForm):
    class Meta:
        model = projectdetail
        fields="__all__"