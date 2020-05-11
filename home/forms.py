from .models import *
from django import forms

class HomeForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = '__all__'
