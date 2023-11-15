from django import forms
from core.models import *

class SagaForm(forms.ModelForm):
    class Meta:
        model = Saga
        fields = ['number', 'title', 'plot']
        
class ArcForm(forms.ModelForm):
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga']
        
class VolumeForm(forms.ModelForm):
    class Meta:
        model = Volume
        fields = ['number', 'title', 'date', 'plot', 'cover']
        
class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc', 'characters']
        
class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['number', 'plot', 'start_date', 'end_date']
        
class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'plot', 'season', 'characters']
        
class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['name', 'description']
        
class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'status', 'species', 'manga_debut', 'anime_debut']