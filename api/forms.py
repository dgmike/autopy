from .models import *
from django import forms

class VehicleTypeForm(forms.ModelForm):
  class Meta:
    model = VehicleType
    fields = ['name']
    labels = {
      'name': 'nome'
    }
    error_messages = {
      'name': {
        'required': 'nome é um campo obrigatório',
        'max_length': 'nome muito grande',
      },
    }
