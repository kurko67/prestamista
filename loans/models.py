from django.db import models
from enum import Enum
from users.models import User
from clients.models import Client

class OrderStatus(Enum):
 	CREATED = 'CREATED'
 	PAYED = 'PAYED'
 	LEGAL = 'LEGAL'

choices = [( tag, tag.value ) for tag in OrderStatus ]

class Loan(models.Model):
    #un cliente, muchos creditos
    client = models.ForeignKey(Client, on_delete = models.CASCADE) #cliente
    user = models.ForeignKey(User, on_delete = models.CASCADE) #usuario que hizo el credito
    money = models.DecimalField(default=0, max_digits=8, decimal_places=2) #monto prestado
    plan = models.IntegerField(default=0) #cantidad de cuotas
    fee_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2) # monto de cuota
    produced = models.DecimalField(default=0, max_digits=8, decimal_places=2) # monto total producido
    seller = models.CharField(max_length=100, null=True, blank= True) #vendedor puntero
    commission = models.DecimalField(default=0, max_digits=8, decimal_places=2) # comision pagada
    commission_payment = models.DateTimeField() #fecha de pago comision
    payment_method = models.CharField(max_length=100, default='MUTUAL') #metodo de pago predeterminado
    status = models.CharField(max_length=50,default='CREATED') #estado del credito
    observations = models.CharField(max_length=500) #observaciones
    ending = models.DateTimeField() #fecha de finalizacion
    created_at = models.DateTimeField(auto_now_add=True) #fecha creacion
    update_at = models.DateTimeField(auto_now_add=True) #fecha de actualizacion

    

class Dues(models.Model):
    #un credito, muchas cuotas
    client = models.ForeignKey(Client, on_delete = models.CASCADE) #cliente
    loan_id = models.ForeignKey(Loan, on_delete = models.CASCADE) #identificacion del credito
    share = models.IntegerField(default=0) #numero de cuota
    fee_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2) # monto de cuota
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=2) # saldo de cuota
    compensatory_interest = models.DecimalField(default=0, max_digits=8, decimal_places=2) # interes compensatorio
    amortization = models.DecimalField(default=0, max_digits=8, decimal_places=2) # amortizacion de cuota
    month_fee = models.CharField(max_length=50) #mes de la cuotas
    year_fee = models.CharField(max_length=50) #año de la cuotas
    fee_payment = models.DateTimeField() #fecha de pago de cuota
    observations = models.CharField(max_length=500) #observaciones
    way_to_pay = models.CharField(max_length=100) #forma de pago
    receipt = models.IntegerField(default=0) #numero de recibo en caso de pago por caja
