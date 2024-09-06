from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria", 'usuario')
    list_editable = ("publicada",)
    list_per_page = 10
    
    # Acima tivemos uma Classe para configurar a pagina de admin do Django na parte referente as fotografias
    # list_display: Campos que serão mostrados no display principal
    # list_display_links: Onde poderá clicar para encaminhar para a página de configuração do produto
    # search_fields: Campo de pesquisa, onde será procurado pela categoria especificada, nesse caso o nome
    # list_filter: Tipos de filtros presentes
    # list_iditable: permite que a edição de tal campo seja feito no próprio display
    # list_per_page: nos ajuda a controlar quantos produtos serão exibidos por página no adm

admin.site.register(Fotografia, ListandoFotografias)
