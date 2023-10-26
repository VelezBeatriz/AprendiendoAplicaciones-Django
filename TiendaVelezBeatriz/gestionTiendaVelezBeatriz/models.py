from django.db import models

# Create your models here.

# Creacion de la classe fabricante
class Fabricante(models.Model):
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    email=models.EmailField()

# Cada clase posteriormente será una tabla
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    fabricante=models.ForeignKey(Fabricante, on_delete=models.CASCADE)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregador=models.BooleanField()
