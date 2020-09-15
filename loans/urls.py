from django.urls import path
from . import views

# Create your views here.
app_name = 'loans' #es para evitar el conflicto de nombres entre rutas

urlpatterns = [

	path('<int:pk>', views.LoansView.as_view(), name='loans_list'),
	path('nuevo_credito',views.create , name='loans_create'),
	#path('crear', views.create, name='create_loan'),
]
