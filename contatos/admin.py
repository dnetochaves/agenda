from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'descricao', 'categoria', 'mostrar')
    
    list_display_links = ('nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
