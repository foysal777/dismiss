from django import forms
from .models import a_model


class a_form(forms.ModelForm):
    class Meta:
        model = a_model
        fields = '__all__' 
        
  
    