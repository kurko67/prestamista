from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)

class Customer(User):
	class Meta:
		proxy = True
