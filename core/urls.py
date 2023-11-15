from django.urls import path
from .views_core import home, docs, about
from .views_saga import SagaListView, SagaCreateView, SagaUpdateView, SagaDeleteView
from .views_arc import ArcListView, ArcCreateView, ArcUpdateView, ArcDeleteView
from .views_volume import VolumeListView, VolumeCreateView, VolumeUpdateView, VolumeDeleteView
from .views_manga import MangaListView, MangaCreateView, MangaUpdateView, MangaDeleteView
from .views_season import SeasonListView, SeasonCreateView, SeasonUpdateView, SeasonDeleteView
from .views_anime import AnimeListView, AnimeCreateView, AnimeUpdateView, AnimeDeleteView
from .views_species import SpeciesListView, SpeciesCreateView, SpeciesUpdateView, SpeciesDeleteView
from .views_character import CharacterListView, CharacterCreateView, CharacterUpdateView, CharacterDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('docs/', docs, name='docs'),
    path('about/', about, name='about'),
    # Saga
    path('saga/', SagaListView.as_view(), name='saga_list'),
    path('saga/create/', SagaCreateView.as_view(), name='saga_create'),
    path('saga/update/<int:number>/', SagaUpdateView.as_view(), name='saga_update'),
    path('saga/delete/<int:number>/', SagaDeleteView.as_view(), name='saga_delete'),
    # Arc
    path('arc/', ArcListView.as_view(), name='arc_list'),
    path('arc/create/', ArcCreateView.as_view(), name='arc_create'),
    path('arc/update/<int:number>/', ArcUpdateView.as_view(), name='arc_update'),
    path('arc/delete/<int:number>/', ArcDeleteView.as_view(), name='arc_delete'),
    # Volume
    path('volume/', VolumeListView.as_view(), name='volume_list'),
    path('volume/create/', VolumeCreateView.as_view(), name='volume_create'),
    path('volume/update/<int:number>/', VolumeUpdateView.as_view(), name='volume_update'),
    path('volume/delete/<int:number>/', VolumeDeleteView.as_view(), name='volume_delete'),
    # Manga
    path('manga/', MangaListView.as_view(), name='manga_list'),
    path('manga/create/', MangaCreateView.as_view(), name='manga_create'),
    path('manga/update/<int:number>/', MangaUpdateView.as_view(), name='manga_update'),
    path('manga/delete/<int:number>/', MangaDeleteView.as_view(), name='manga_delete'),
    # Season
    path('season/', SeasonListView.as_view(), name='season_list'),
    path('season/create/', SeasonCreateView.as_view(), name='season_create'),
    path('season/update/<int:number>/', SeasonUpdateView.as_view(), name='season_update'),
    path('season/delete/<int:number>/', SeasonDeleteView.as_view(), name='season_delete'),
    # Anime
    path('anime/', AnimeListView.as_view(), name='anime_list'),
    path('anime/create/', AnimeCreateView.as_view(), name='anime_create'),
    path('anime/update/<int:number>/', AnimeUpdateView.as_view(), name='anime_update'),
    path('anime/delete/<int:number>/', AnimeDeleteView.as_view(), name='anime_delete'),
    # Species
    path('species/', SpeciesListView.as_view(), name='species_list'),
    path('species/create/', SpeciesCreateView.as_view(), name='species_create'),
    path('species/update/<int:number>/', SpeciesUpdateView.as_view(), name='species_update'),
    path('species/delete/<int:number>/', SpeciesDeleteView.as_view(), name='species_delete'),
    # Character
    path('character/', CharacterListView.as_view(), name='character_list'),
    path('character/create/', CharacterCreateView.as_view(), name='character_create'),
    path('character/update/<int:number>/', CharacterUpdateView.as_view(), name='character_update'),
    path('character/delete/<int:number>/', CharacterDeleteView.as_view(), name='character_delete'),
]