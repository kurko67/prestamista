from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Loan
from .forms import LoanForm
#from .forms import ClientForm
from django.urls import reverse_lazy
from django.db.models import Q #para trabajar con una consulta con dist. filtros
from django.shortcuts import get_object_or_404


class LoansView(ListView):
	template_name = 'loans/list_loans.html'
	model = Loan

	def get_queryset(self):  # no pk parameter
		cliente = get_object_or_404(Loan, pk=self.kwargs['pk'])
		return self.model.objects.filter(client=cliente.id)

@login_required(login_url='login')
def create(request):
	form = LoanForm(request.POST)#siempre y cuando sea POST
	if request.method == 'POST' and form.is_valid():
		form.save()
		messages.success(request, 'Credito creado con exito')
		return redirect('clients:client_list')

	return render(request, 'loans/create.html',{
			'form': form
		})
