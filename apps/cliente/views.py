from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from .forms import ClienteForm
from .models import Cliente


class Dashboard(TemplateView):
    template_name = 'dashboard/index.html'


class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    paginate_by = 5


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_list')
    # messages.add_message(request, messages.INFO, 'Hello world.')


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_list')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente:cliente_list')
