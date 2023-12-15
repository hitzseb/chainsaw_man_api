import os
from django.http import Http404
from django.views.static import serve
from django.conf import settings

# Serve images
def serve_image(request, image_filename):
    # build image file path
    image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

    # Verify if file exists
    if not os.path.exists(image_path):
        raise Http404(f"Image does not exist at {image_path}")

    # Configure Content-Disposition header
    response = serve(request, os.path.relpath(image_path, settings.MEDIA_ROOT), document_root=settings.MEDIA_ROOT)

    return response