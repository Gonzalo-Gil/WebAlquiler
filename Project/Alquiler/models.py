from django.db import models

# Create your models here.

class TipoCombo(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
    
class Combo(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(null=True)
    price = models.IntegerField(null=False, blank=False)
    productos = models.ManyToManyField(Producto)
    type = models.ForeignKey(TipoCombo, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
