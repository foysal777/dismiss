from django.shortcuts import render, redirect, get_object_or_404
from musician_app.models import musicModel
from album_app.models import albumModel
from musician_app import forms

def home(request):
    return render(request, 'home.html')

def database(request):
    combined_data = musicModel.objects.select_related('album').all()
    
    data_list = [{
        'id': item.id,
        'musician_name': f"{item.first_name} {item.last_name}",
        'email': item.email,
        'instrument': item.instrument,
        'album_name': item.album.album_name,
        'album_rating': item.album.album_rating,
        'release_date': item.album.album_release_date,
    } for item in combined_data]
    
    return render(request, 'database.html', {'data': data_list})

def edit_album(request, id):
    edit = get_object_or_404(albumModel, pk=id)
    my_form = forms.AForm(instance=edit)
    if request.method == "POST":
        my_form = forms.AForm(request.POST, instance=edit)
        if my_form.is_valid():
            my_form.save()
            return redirect('database')
    
    return render(request, 'album.html', {'data': my_form})

def edit_name(request, id):
    edit = get_object_or_404(musicModel, pk=id)
    my_form = forms.MForm(instance=edit)
    if request.method == "POST":
        my_form = forms.MForm(request.POST, instance=edit)
        if my_form.is_valid():
            my_form.save()
            return redirect('database')
    
    return render(request, 'musician.html', {'data': my_form})

def delete_post(request, id):
    edit = get_object_or_404(musicModel, pk=id)
    edit.delete()
    return redirect('database')
