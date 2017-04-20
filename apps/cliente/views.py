from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.cliente.forms import ClienteForm
from apps.cliente.models import Cliente

# Create your views here.
def index(request):
    return render(request, 'cliente/index.html')

class ClienteList(ListView):
	model = Cliente
	template_name = 'cliente/cliente_list.html'
	paginate_by = 5

class ClienteCreate(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_list')

class ClienteUpdate(UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_list')

class ClienteDelete(DeleteView):
	model = Cliente
	template_name = 'cliente/cliente_delete.html'
	success_url = reverse_lazy('cliente:cliente_list')
