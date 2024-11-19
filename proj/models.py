from django.db import models
from decimal import Decimal

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True) 
    author = models.CharField(max_length=100, unique=True) # até 100 caracteres
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  #máximo 10 dígitos, e 2 casas decimais após a vírgula.
    pages = models.IntegerField() #numero inteiro

    class Meta:
        ordering = ['published_date'] #ordem por data de publicação

    def __str__(self):
        return self.title
# Create your models here.

