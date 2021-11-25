from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)    
    data_nascimento = models.DateField(null=False, blank=False)
    login = models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome