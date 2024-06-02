from django import forms
from .models import m_model


class m_form(forms.ModelForm):
    class Meta:
        model = m_model
        fields = '__all__' 
  
    