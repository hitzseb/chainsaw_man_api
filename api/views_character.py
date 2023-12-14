import os
from django.http import Http404
from django.views.static import serve
from django.conf import settings
from .serializers import CharacterSerializer, CharacterSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Character

# Get all characters
class CharacterListView(ListAPIView):
    queryset = Character.objects.order_by('manga_debut__number')
    serializer_class = CharacterSerializerSm
    
# Get character by name
class CharacterRetrieveView(RetrieveAPIView):
    serializer_class = CharacterSerializer
    lookup_field = 'name'
    
    def get_queryset(self):
        name = self.kwargs['name']
        return Character.objects.filter(name=name)
    
# Serve character picture
def serve_character_picture(request, image_filename):
    # build image file path
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

    # Verify if file exists
    if not os.path.exists(image_path):
        raise Http404(f"Image does not exist at {image_path}")

    # Configure Content-Disposition header
    response = serve(request, os.path.relpath(image_path, settings.MEDIA_ROOT), document_root=settings.MEDIA_ROOT)

    return response