from django.db import models
from django.db.models.signals import pre_save
import uuid


class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    document = models.CharField(max_length=8)
    cuil = models.CharField(max_length=13)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    home = models.CharField(max_length=200)
    locality = models.CharField(max_length=100)
    province = models.CharField(max_length=100, default = 'Mendoza')
    postal_code = models.CharField(max_length=4)
    nationality = models.CharField(max_length=100, default='Argentino')
    work = models.CharField(max_length=300)
    work_address = models.CharField(max_length=400)
    work_phone = models.CharField(max_length=15)
    ingresos = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    foto_dni = models.ImageField(upload_to='dni/', null=True, blank=True)
    email = models.EmailField()
    create_at = models.DateTimeField(auto_now= True)
    male_female = models.CharField(max_length=50)
    client_id = models.CharField(max_length=100, null=False, blank= False, unique=True)

    def __str__(self):
        return self.name + ' ' + self.surname

def set_client_id(sender, instance, *args, **kwargs):
    if not instance.client_id:
        instance.client_id = str(uuid.uuid4())


pre_save.connect(set_client_id, sender=Client)
