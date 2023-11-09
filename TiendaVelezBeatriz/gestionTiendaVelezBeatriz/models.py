from django.db import models

# Create your models here.

# Creacion de la classe fabricante
class Fabricante(models.Model):
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    email=models.EmailField()
    
    def __str__(self):
        return 'El fabricante se llama %s %s y su correo electrónico es %s' % (self.nombre, self.apellidos, self.email)

# Cada clase posteriormente será una tabla
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return 'El cliente se llama %s, vive en %s. Puedes contactarlo desde %s o %s' % (self.nombre, self.direccion, self.email, self.telefono)

    
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    fabricante=models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return 'Fabricante del pedido %s %s.El nombre es %s, la sección es %s y el precio es %s' % (self.fabricante.nombre, self.fabricante.apellidos, self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregador=models.BooleanField()

    def __str__(self):
        if self.entregador:
            return 'El pedido nº%s ha sido entregado el día %s' % (self.numero, self.fecha)
        else:
            return 'El pedido no ha sido entregado'

   


