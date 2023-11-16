from django.db import models

# Create your models here.

# Creacion de la classe fabricante
class Fabricante(models.Model):
    nombre=models.CharField(max_length=30, verbose_name="Nombre del fabricante")
    apellidos=models.CharField(max_length=30, verbose_name="Primer y segundo apellido")
    email=models.EmailField(verbose_name="Correo electrónico")
    
    def __str__(self):
        return 'El fabricante  %s %s tiene este correo electrónico %s' % (self.nombre, self.apellidos, self.email)

# Cada clase posteriormente será una tabla
class Clientes(models.Model):
    nombre=models.CharField(max_length=30, verbose_name="Nombre del cliente")
    direccion=models.CharField(max_length=50, verbose_name="Dirección")
    email=models.EmailField(blank=True, null=True, verbose_name="Correo electrónico" )
    telefono=models.CharField(max_length=7, verbose_name="Teléfono")

    def __str__(self):
        return 'El cliente %s, vive en %s. Sus contactos son %s o %s' % (self.nombre, self.direccion, self.email, self.telefono)

    
class Articulos(models.Model):
    nombre=models.CharField(max_length=30,verbose_name="Nombre del artículo")
    seccion=models.CharField(max_length=20,verbose_name="Sección")
    precio=models.IntegerField(verbose_name="Precio en €")
    fabricante=models.ForeignKey(Fabricante, on_delete=models.CASCADE, verbose_name="Identificador del fabricante")

    def __str__(self):
        return 'El fabricante del pedido es %s %s.El articulo es %s, su sección es %s y su precio es %s' % (self.fabricante.nombre, self.fabricante.apellidos, self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField(verbose_name="Número del pedido")
    fecha=models.DateField(verbose_name="Fecha de entrega")
    entregador=models.BooleanField(verbose_name="Entregado o no")

    def __str__(self):
        if self.entregador:
            return 'El pedido nº%s ha sido entregado el día %s' % (self.numero, self.fecha)
        else:
            return 'El pedido nº%s no ha sido entregado' % (self.numero)

   


