from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def musician(request):
    if request.method == "POST":
        my_form = forms.m_form(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect ('musician')
    
    
    else :
        my_form = forms.m_form()
    return render(request, 'musician.html', {'data' : my_form })


    