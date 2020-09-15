from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client
from .forms import ClientForm
from django.urls import reverse_lazy
from django.db.models import Q #para trabajar con una consulta con dist. filtros


class ClientListView(LoginRequiredMixin, ListView):
	login_url = 'login'
	model = Client
	template_name = 'clients/list_client.html'
	paginate_by = 10

	def get_queryset(self):
		return Client.objects.all()


@login_required(login_url='login')
def create(request):
	form = ClientForm(request.POST)#siempre y cuando sea POST
	if request.method == 'POST' and form.is_valid():
		form.save()
		messages.success(request, 'Cliente creado con exito')
		return redirect('clients:client_list')

	return render(request, 'clients/create.html',{
			'form': form
		})

class UpdateClient(LoginRequiredMixin, UpdateView):
	model = Client
	form_class = ClientForm
	template_name = 'clients/create.html'
	success_url = reverse_lazy('clients:client_list')

class ClientView(LoginRequiredMixin, DetailView):
	model = Client
	template_name = 'clients/view.html'


class ClientSearchListView(ListView):
	template_name = 'clients/list_client.html'

	def get_queryset(self):
		#es como poner en sql select * from products like %value% = __icontains
		filters = Q(name__icontains=self.query()) | Q(surname__icontains=self.query())
		return Client.objects.filter(filters)

	def query(self):
		return self.request.GET.get('q')


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['query'] = self.query()
		context['count'] = context['client_list'].count()

		return context
