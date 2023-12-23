from django import forms
from .models import Motorcycle

# forms.py
class MotorcycleForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['brand', 'model', 'year', 'max_speed']
        exclude = ['id']
