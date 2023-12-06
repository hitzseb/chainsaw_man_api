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
        
# MangaForm

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'volume', 'arc', 'characters']
        
# SeasonForm

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['number', 'plot', 'start_date', 'end_date']
        
# AnimeForm

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'season', 'characters']
        
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