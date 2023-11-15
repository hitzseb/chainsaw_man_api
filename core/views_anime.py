from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Anime
from .forms import AnimeForm

# List anime

class AnimeListView(AdminRequiredMixin, ListView):
    model = Anime
    template_name = 'list_anime.html'
    context_object_name = 'anime_list'

# Create anime

class AnimeCreateView(AdminRequiredMixin, CreateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'form.html'
    success_url = '/anime/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Anime'
        return context

# Update anime

class AnimeUpdateView(AdminRequiredMixin, UpdateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'form.html'
    context_object_name = 'anime'
    success_url = '/anime/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete anime

class AnimeDeleteView(AdminRequiredMixin, DeleteView):
    model = Anime
    template_name = 'confirm_delete.html'
    success_url = '/anime/'