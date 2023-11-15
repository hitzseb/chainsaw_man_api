from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Arc
from .forms import ArcForm

# List arc

class ArcListView(AdminRequiredMixin, ListView):
    model = Arc
    template_name = 'list_arc.html'
    context_object_name = 'arc_list'

# Create arc

class ArcCreateView(AdminRequiredMixin, CreateView):
    model = Arc
    form_class = ArcForm
    template_name = 'form.html'
    success_url = '/arc/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Arc'
        return context

# Update arc

class ArcUpdateView(AdminRequiredMixin, UpdateView):
    model = Arc
    form_class = ArcForm
    template_name = 'form.html'
    context_object_name = 'arc'
    pk_url_kwarg = 'number'
    success_url = '/arc/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete arc

class ArcDeleteView(AdminRequiredMixin, DeleteView):
    model = Arc
    pk_url_kwarg = 'number'
    success_url = '/arc/'