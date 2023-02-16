from django.db import models

# Create your models here.

class Sessao (models.Model):
    nome = models.CharField (max_length=100)

    def __str__ (self):
        return self.nome

class Produto (models.Model):
    descricao = models.CharField (max_length=100)
    preco = models.CharField (max_length=100)
    sessao = models.ForeignKey (Sessao, on_delete=models.CASCADE)

    def __str__ (self):
        return self.descricao
