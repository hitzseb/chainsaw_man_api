from django import forms
from core.models import *

# SagaForm

class SagaForm(forms.ModelForm):
    class Meta:
        model = Saga
        fields = ['number', 'title', 'plot']
        
# ArcForm

class ArcForm(forms.ModelForm):
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga']
        
# VolumeForm

class VolumeForm(forms.ModelForm):
    class Meta:
        model = Volume
        fields = ['number', 'title', 'date', 'cover', 'plot']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
# MangaForm

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'volume', 'arc', 'characters']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'characters': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 300px;'}),
        }
        
# SeasonForm

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['number', 'plot', 'start_date', 'end_date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
# AnimeForm

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'season', 'characters']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'characters': forms.SelectMultiple(attrs={'class': 'form-control', 'style': 'height: 300px;'}),
        }
        
# SpeciesForm

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['name', 'description']
        
# CharacterForm

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'status', 'species', 'manga_debut', 'anime_debut', 'seiyu']