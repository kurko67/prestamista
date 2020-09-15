from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
			'name', 'surname', 'document', 'cuil', 'birthday','mobile','phone',
            'home', 'locality', 'province', 'postal_code', 'nationality', 'work',
            'work_address', 'ingresos', 'foto_dni', 'email', 'male_female'
		]

        labels = {
			'name': 'Nombre',
			'surname': 'Apellido',
			'document': 'DNI',
			'cuil': 'Cuil',
			'birthday': 'Fecha de nacimiento',
			'mobile': 'Celular',
			'phone': 'Telefono fijo',
            'home': 'Domicilio',
            'locality': 'Localidad',
            'province': 'Provincia',
            'postal_code': 'Codigo Postal',
            'nationality': 'Nacionalidad',
            'work': 'Lugar de trabajo',
            'work_address': 'Domicilio laboral',
            'ingresos': 'Ingresos',
            'foto_dni': 'Foto documento',
            'email': 'Correo electronico',
            'male_female':'Genero'
		}


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'surname': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'document': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'8'}),
            'cuil': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'13'}),
            'birthday': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'13','type':'date'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'20'}),
            'phone': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'15'}),
            'nationality': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'25'}),
            'home': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
            'locality': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'4'}),
            'province': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'7'}),
            'work': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
            'work_address': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
            'email': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'150','type':'email'}),
            'ingresos': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'150','type':'number'}),
            'male_female': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'150','type':'select'}),
        }
