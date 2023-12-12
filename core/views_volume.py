import os
from django.http import Http404

from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Volume
from .forms import VolumeForm
from django.views.static import serve
from django.conf import settings

# List volume

class VolumeListView(AdminRequiredMixin, ListView):
    model = Volume
    template_name = 'list_volume.html'
    context_object_name = 'volume_list'

# Create volume

class VolumeCreateView(AdminRequiredMixin, CreateView):
    model = Volume
    form_class = VolumeForm
    template_name = 'form.html'
    success_url = '/volume/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Volume'
        return context

# Update volume

class VolumeUpdateView(AdminRequiredMixin, UpdateView):
    model = Volume
    form_class = VolumeForm
    template_name = 'form.html'
    context_object_name = 'volume'
    success_url = '/volume/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete volume

class VolumeDeleteView(AdminRequiredMixin, DeleteView):
    model = Volume
    template_name = 'confirm_delete.html'
    success_url = '/volume/'
    
def serve_volume_cover(request, image_filename):
    # build image file path
    image_path = os.path.join(settings.MEDIA_ROOT, 'volume_covers', image_filename)

    # Verify if file exists
    if not os.path.exists(image_path):
        raise Http404(f"Image does not exist at {image_path}")

    # Configure Content-Disposition header
    response = serve(request, os.path.relpath(image_path, settings.MEDIA_ROOT), document_root=settings.MEDIA_ROOT)

    return response