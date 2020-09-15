from django.contrib import admin
from .models import Client

#class ClientAdmin(admin.ModelAdmin):
#	fields = ('name','surname','document', 'home')
#	list_display = ('name','surname','document', 'home')

admin.site.register(Client)

# Register your models here.
