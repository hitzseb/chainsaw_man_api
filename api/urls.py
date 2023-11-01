from django.urls import path
from .views import *

urlpatterns = [
    # saga urls
    path('saga/', SagaListView.as_view(), name='saga-list'),
    path('saga/create', SagaCreateView.as_view(), name='saga-create'),
    path('saga/update/<int:number>/', SagaUpdateView.as_view(), name='saga-update'),
    path('saga/destroy/<int:number>/', SagaDestroyView.as_view(), name='saga-destroy'),
    # arc urls
    path('arc/', ArcListView.as_view(), name='arc-list'),
    path('arc/create', ArcCreateView.as_view(), name='arc-create'),
    path('arc/update/<int:number>/', ArcUpdateView.as_view(), name='arc-update'),
    path('arc/destroy/<int:number>/', ArcDestroyView.as_view(), name='arc-destroy'),
    # volume urls
    path('volume/', VolumeListView.as_view(), name='volume-list'),
    path('volume/create', VolumeCreateView.as_view(), name='volume-create'),
    path('volume/update/<int:number>/', VolumeUpdateView.as_view(), name='volume-update'),
    path('volume/destroy/<int:number>/', VolumeDestroyView.as_view(), name='volume-destroy'),
    # manga urls
    path('manga/', MangaListView.as_view(), name='manga-list'),
    path('manga/detail/<int:number>/', MangaRetrieveView.as_view(), name='manga-retrieve'),
    path('manga/create', MangaCreateView.as_view(), name='manga-create'),
    path('manga/update/<int:number>/', MangaUpdateView.as_view(), name='manga-update'),
    path('manga/destroy/<int:number>/', MangaDestroyView.as_view(), name='manga-destroy'),
    # character urls
    path('character/', CharacterListView.as_view(), name='character-list'),
    path('character/detail/<str:name>/', CharacterRetrieveView.as_view(), name='character-retrieve'),
    path('character/create', CharacterCreateView.as_view(), name='character-create'),
    path('character/update/<str:name>/', CharacterUpdateView.as_view(), name='character-update'),
    path('character/destroy/<str:name>/', CharacterDestroyView.as_view(), name='character-destroy'),
]