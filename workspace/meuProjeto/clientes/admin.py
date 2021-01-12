from django.contrib import admin
from .models import Cliente, Telefone, CPF

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(CPF)