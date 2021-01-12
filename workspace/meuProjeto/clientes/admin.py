from django.contrib import admin
from .models import Cliente, Telefone, CPF, Produto

# Register your models here.

# fields
# list_display
# list_filter
# search_fields

class ClienteAdmin(admin.ModelAdmin):
    # Determina os campos que serão mostrados
    fields = ('name', 'endereco')
    # Determina quais os campos que serão mostrados no grid
    list_display = ('id', 'name', 'endereco', 'email')
    # Permite que você filtre os dados por um determinado campo
    list_filter = ('produtos',)
    # Cria uma forma de pesquisar os dados
    search_fields = ('id', 'name', 'email', 'produtos__name')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Produto)