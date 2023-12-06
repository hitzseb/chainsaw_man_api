from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Season
from .forms import SeasonForm

# List season

class SeasonListView(AdminRequiredMixin, ListView):
    model = Season
    template_name = 'list_season.html'
    context_object_name = 'season_list'

# Create season

class SeasonCreateView(AdminRequiredMixin, CreateView):
    model = Season
    form_class = SeasonForm
    template_name = 'form.html'
    success_url = '/season/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Season'
        return context

# Update season

class SeasonUpdateView(AdminRequiredMixin, UpdateView):
    model = Season
    form_class = SeasonForm
    template_name = 'form.html'
    context_object_name = 'season'
    success_url = '/season/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete season

class SeasonDeleteView(AdminRequiredMixin, DeleteView):
    model = Season
    template_name = 'confirm_delete.html'
    success_url = '/season/'