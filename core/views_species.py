from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Species
from .forms import SpeciesForm

# List species

class SpeciesListView(AdminRequiredMixin, ListView):
    model = Species
    template_name = 'list_species.html'
    context_object_name = 'species_list'

# Create species

class SpeciesCreateView(AdminRequiredMixin, CreateView):
    model = Species
    form_class = SpeciesForm
    template_name = 'form.html'
    success_url = '/species/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Species'
        return context

# Update species

class SpeciesUpdateView(AdminRequiredMixin, UpdateView):
    model = Species
    form_class = SpeciesForm
    template_name = 'form.html'
    context_object_name = 'species'
    pk_url_kwarg = 'name'
    success_url = '/species/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete species

class SpeciesDeleteView(AdminRequiredMixin, DeleteView):
    model = Species
    pk_url_kwarg = 'name'
    success_url = '/species/'