from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = [
			'client', 'user', 'money', 'plan', 'fee_amount','produced','seller',
            'commission', 'commission_payment', 'payment_method', 'status', 'observations', 'ending'
		]

        labels = {
			'client': 'Cliente',
			'user': 'Usuario',
			'money': 'Monto a prestar',
			'plan': 'cuotas',
			'fee_amount': 'Monto de cuotas',
			'produced': 'Total Credito',
			'seller': 'Vendedor',
            'commission': 'Comision',
            'commission_payment': 'Pago comision',
            'payment_method': 'Forma de pago',
            'status': 'Estado',
            'observations': 'observaciones',
            'ending': 'finalizacion'
		}


        widgets = {
            'client': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'user': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'money': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'8'}),
            'plan': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'13'}),
            'fee_amount': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'13','type':'date'}),
            'produced': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'20'}),
            'seller': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'15'}),
            'commission': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'25'}),
            'commission_payment': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
            'payment_method': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
            'status': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'4'}),
            'observations': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'7'}),
            'ending': forms.TextInput(attrs={'class':'form-control','required':'true','data-val-length-max':'500'}),
        }
