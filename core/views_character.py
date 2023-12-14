from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Character
from .forms import CharacterForm

# List character
class CharacterListView(AdminRequiredMixin, ListView):
    model = Character
    template_name = 'list_character.html'
    context_object_name = 'character_list'
    
    def get_queryset(self):
        return Character.objects.order_by('manga_debut__number')

# Create character
class CharacterCreateView(AdminRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'form.html'
    success_url = '/character/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Character'
        return context

# Update character
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

# Delete character
class CharacterDeleteView(AdminRequiredMixin, DeleteView):
    model = Character
    template_name = 'confirm_delete.html'
    success_url = '/character/'