from django.contrib import admin

# Register your models here.
from gestionTiendaVelezBeatriz.models import Clientes, Fabricante ,Articulos, Pedidos

#Create list display administration panel
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "email", "telefono")
    search_fields=("email", "telefono")

class FabricanteAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellidos", "email")
    search_fields=("nombre", "apellidos")

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    search_fields=("nombre", "seccion", "precio")

class PedidoseAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregador")
    search_fields=("numero", "fecha", "entregador")


# Register models on database
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidoseAdmin)




