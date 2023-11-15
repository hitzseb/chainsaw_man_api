from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Volume
from .forms import VolumeForm

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
    pk_url_kwarg = 'number'
    success_url = '/volume/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete volume

class VolumeDeleteView(AdminRequiredMixin, DeleteView):
    model = Volume
    pk_url_kwarg = 'number'
    success_url = '/volume/'