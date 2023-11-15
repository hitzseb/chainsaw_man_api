from .views_core import AdminRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Saga
from .forms import SagaForm

# List saga

class SagaListView(AdminRequiredMixin, ListView):
    model = Saga
    template_name = 'list_saga.html'
    context_object_name = 'saga_list'

# Create saga

class SagaCreateView(AdminRequiredMixin, CreateView):
    model = Saga
    form_class = SagaForm
    template_name = 'form.html'
    success_url = '/saga/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Create Saga'
        return context

# Update saga

class SagaUpdateView(AdminRequiredMixin, UpdateView):
    model = Saga
    form_class = SagaForm
    template_name = 'form.html'
    context_object_name = 'manga'
    pk_url_kwarg = 'number'
    success_url = '/saga/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = f'{self.object}'
        return context

# Delete saga

class SagaDeleteView(AdminRequiredMixin, DeleteView):
    model = Saga
    pk_url_kwarg = 'number'
    success_url = '/saga/'