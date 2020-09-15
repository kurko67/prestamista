from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='avatar/users/', null=False, blank=False)

class Customer(User):
	class Meta:
		proxy = True
