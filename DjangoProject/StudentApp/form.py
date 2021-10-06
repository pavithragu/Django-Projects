from django import forms
from StudentApp.models import Students


class fdetails(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
