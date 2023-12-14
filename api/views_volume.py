import os
from django.http import Http404
from django.views.static import serve
from django.conf import settings
from .serializers import VolumeSerializer, VolumeSerializerSm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Volume

# Get all volumes
class VolumeListView(ListAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializerSm
    
# Get volume by number
class VolumeRetrieveView(RetrieveAPIView):
    serializer_class = VolumeSerializer
    lookup_field = 'number'
    
    def get_queryset(self):
        number = self.kwargs['number']
        return Volume.objects.filter(number=number)
    
# Serve volume cover
def serve_volume_cover(request, image_filename):
    # build image file path
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

    # Verify if file exists
    if not os.path.exists(image_path):
        raise Http404(f"Image does not exist at {image_path}")

    # Configure Content-Disposition header
    response = serve(request, os.path.relpath(image_path, settings.MEDIA_ROOT), document_root=settings.MEDIA_ROOT)

    return response