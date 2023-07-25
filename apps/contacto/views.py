from typing import Any, Dict
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView

from . import models, forms


# Create your views here.

class ContactoCreateView(CreateView):
    model = models.Contacto
    template_name = 'contacto/forms/contacto.html'
    form_class = forms.ContactoForm
    success_url = reverse_lazy('apps.contacto:contacto')

    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context