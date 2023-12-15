from django.urls import path
from .views_saga import SagaListView, SagaRetrieveView
from .views_arc import ArcListView, ArcRetrieveView
from .views_volume import VolumeListView, VolumeRetrieveView
from .views_manga import MangaListView, MangaRetrieveView
from .views_season import SeasonListView, SeasonRetrieveView
from .views_anime import AnimeListView, AnimeRetrieveView
from .views_species import SpeciesListView, SpeciesRetrieveView
from .views_character import CharacterListView, CharacterRetrieveView
from .views_media import serve_image

urlpatterns = [
    path('saga/', SagaListView.as_view(), name='saga_list_drf'),
    path('saga/<int:number>/', SagaRetrieveView.as_view(), name='saga_detail_drf'),
    path('arc/', ArcListView.as_view(), name='arc_list_drf'),
    path('arc/<int:number>/', ArcRetrieveView.as_view(), name='arc_detail_drf'),
    path('volume/', VolumeListView.as_view(), name='volume_list_drf'),
    path('volume/<int:number>/', VolumeRetrieveView.as_view(), name='volume_detail_drf'),
    path('volume/cover/<str:image_filename>/', serve_image, name='serve_volume_cover'),
    path('manga/', MangaListView.as_view(), name='manga_list_drf'),
    path('manga/<int:number>/', MangaRetrieveView.as_view(), name='manga_detail_drf'),
    path('manga/cover/<str:image_filename>/', serve_image, name='serve_manga_cover'),
    path('season/', SeasonListView.as_view(), name='season_list_drf'),
    path('season/<int:number>/', SeasonRetrieveView.as_view(), name='season_detail_drf'),
    path('season/poster/<str:image_filename>/', serve_image, name='serve_season_poster'),
    path('anime/', AnimeListView.as_view(), name='anime_list_drf'),
    path('anime/<str:number>/', AnimeRetrieveView.as_view(), name='anime_detail_drf'),
    path('anime/still/<str:image_filename>/', serve_image, name='serve_manime_still'),
    path('species/', SpeciesListView.as_view(), name='species_list_drf'),
    path('species/<str:name>/', SpeciesRetrieveView.as_view(), name='species_detail_drf'),
    path('character/', CharacterListView.as_view(), name='character_list_drf'),
    path('character/<str:name>/', CharacterRetrieveView.as_view(), name='character_detail_drf'),
    path('character/picture/<str:image_filename>/', serve_image, name='serve_character_picture'),
]