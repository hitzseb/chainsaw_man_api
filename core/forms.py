from django import forms
from core.models import *

# SagaForm

class SagaForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'shadow-none border-dark'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    plot = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}), required=False)
    
    class Meta:
        model = Saga
        fields = ['number', 'title', 'plot']
        
# ArcForm

class ArcForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'shadow-none border-dark'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    plot = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}), required=False)
    saga = forms.ModelChoiceField(
        queryset=Saga.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    
    class Meta:
        model = Arc
        fields = ['number', 'title', 'plot', 'saga']
        
# VolumeForm

class VolumeForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'shadow-none border-dark'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control shadow-none border-dark',
                'type': 'date',
            }
        ),
        required=False,
    )
    cover = forms.URLField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}))
    plot = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}))
    
    class Meta:
        model = Volume
        fields = ['number', 'title', 'date', 'cover', 'plot']
        
# MangaForm

class MangaForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'shadow-none border-dark'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control shadow-none border-dark',
                'type': 'date',
            }
        ),
        required=False,
    )
    cover = forms.URLField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    plot = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}), required=False)
    volume = forms.ModelChoiceField(
        queryset=Volume.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    arc = forms.ModelChoiceField(
        queryset=Arc.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    characters = forms.ModelMultipleChoiceField(
        queryset=Character.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    
    class Meta:
        model = Manga
        fields = ['number', 'title', 'date', 'cover', 'plot', 'volume', 'arc', 'characters']
        
# SeasonForm

class SeasonForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'shadow-none border-dark'}))
    plot = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}), required=False)
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control shadow-none border-dark',
                'type': 'date',
            }
        ),
        required=False,
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control shadow-none border-dark',
                'type': 'date',
            }
        ),
        required=False,
    )
    
    class Meta:
        model = Season
        fields = ['number', 'plot', 'start_date', 'end_date']
        
# AnimeForm

class AnimeForm(forms.ModelForm):
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'shadow-none border-dark'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control shadow-none border-dark',
                'type': 'date',
            }
        ),
        required=False,
    )
    plot = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}))
    season = forms.ModelChoiceField(
        queryset=Season.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    characters = forms.ModelMultipleChoiceField(
        queryset=Character.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    
    class Meta:
        model = Anime
        fields = ['number', 'title', 'date', 'plot', 'season', 'characters']
        
# SpeciesForm

class SpeciesForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}), required=False)
    
    class Meta:
        model = Species
        fields = ['name', 'description']
        
# CharacterForm

class CharacterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}))
    picture = forms.URLField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'shadow-none border-dark'}), required=False)
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    species = forms.ModelChoiceField(
        queryset=Species.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    manga_debut = forms.ModelChoiceField(
        queryset=Manga.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    anime_debut = forms.ModelChoiceField(
        queryset=Anime.objects.all(),
        widget=forms.Select(attrs={'class': 'shadow-none border-dark'}),
        required=False,
    )
    seiyu = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}), required=False)
    
    class Meta:
        model = Character
        fields = ['name', 'picture', 'description', 'status', 'species', 'manga_debut', 'anime_debut', 'seiyu']