from django.urls import path
from . import views

app_name = 'clients' #es para evitar el conflicto de nombres entre rutas

urlpatterns = [

	path('', views.ClientListView.as_view(), name='client_list'),
	path('crear', views.create, name='create'),
	path('editar/<int:pk>', views.UpdateClient.as_view(), name='edit'),
	path('ver/<int:pk>', views.ClientView.as_view(), name='view'),
	path('search', views.ClientSearchListView.as_view(), name='search'),
]
