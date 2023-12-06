from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Manga
from .forms import MangaForm

# List manga

class MangaListView(AdminRequiredMixin, ListView):
    model = Manga
    template_name = 'list_manga.html'
    context_object_name = 'manga_list'

# Create manga

class MangaCreateView(AdminRequiredMixin, CreateView):
    model = Manga
    form_class = MangaForm
    template_name = 'form.html'
    success_url = '/manga/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Manga'
        return context

# Update manga

class MangaUpdateView(AdminRequiredMixin, UpdateView):
    model = Manga
    form_class = MangaForm
    template_name = 'form.html'
    context_object_name = 'manga'
    success_url = '/manga/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete manga

class MangaDeleteView(AdminRequiredMixin, DeleteView):
    model = Manga
    template_name = 'confirm_delete.html'
    success_url = '/manga/'