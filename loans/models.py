from django.db import models
from enum import Enum
from users.models import User

class OrderStatus(Enum):
 	CREATED = 'CREATED'
 	PAYED = 'PAYED'
 	LEGAL = 'LEGAL'

choices = [( tag, tag.value ) for tag in OrderStatus ]

class Loan(models.Model):
    #un cliente, muchos creditos
    loan_id = models.CharField(max_length=100, null=False, blank= False, unique=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    money = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    plan = models.IntegerField(default=0)
    produced = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    seller = models.CharField(max_length=100, null=True, blank= True)
    payment_method = models.CharField(max_length=100, default='MUTUAL')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=choices,default=OrderStatus.CREATED)
    observations = models.CharField(max_length=500)

    
