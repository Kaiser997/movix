from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    apellido = models.CharField(max_length=200, null=False)
    identificacion = models.CharField(max_length=200, null=False)
    correo = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20, null=False)
    saldo = models.FloatField(default=0)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Pago(models.Model):
    valorpago = models.FloatField(default=0,null=False)
    referencia = models.CharField(max_length=200, null=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=False)

class Logcarro(models.Model):
    fecha = models.DateTimeField()
    saldoactual = models.FloatField(default=0)
    saldoposterior = models.FloatField(default=0)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=False)


  