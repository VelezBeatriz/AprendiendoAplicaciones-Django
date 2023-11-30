from django.shortcuts import render
from django.http import HttpResponse
from gestionTiendaVelezBeatriz.models import Articulos, Clientes

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    # Comprobar si is_empty la petición 
    if request.GET["productos"]:

        producto=request.GET["productos"]
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        # mensaje="Artículo buscado:  %r" %request.GET["productos"]

        return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:

        mensaje="No has introducido nada..."

    return HttpResponse(mensaje)

# Para clientes
def busqueda_clientes(request):

    return render(request, "busqueda_clientes.html")


def buscarCliente(request):

    # Comprobar si is_empty la petición 
    if request.GET["clientes"]:

        cliente=request.GET["clientes"]
        ListaClientes=Clientes.objects.filter(nombre__icontains=cliente)

        return render(request, "resultados_busquedaCliente.html", {"clientes":ListaClientes, "query":cliente})

    else:

        mensaje="No has introducido nada..."

    return HttpResponse(mensaje)