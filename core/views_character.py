from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Character
from .forms import CharacterForm

# Character views

class CharacterListView(AdminRequiredMixin, ListView):
    model = Character
    template_name = 'list_character.html'
    context_object_name = 'character_list'

class CharacterCreateView(AdminRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'form.html'
    success_url = '/character/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Character'
        return context

class CharacterUpdateView(AdminRequiredMixin, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'form.html'
    context_object_name = 'character'
    success_url = '/character/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

class CharacterDeleteView(AdminRequiredMixin, DeleteView):
    model = Character
    template_name = 'confirm_delete.html'
    success_url = '/character/'