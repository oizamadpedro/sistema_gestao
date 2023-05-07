from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=30)
    finalizado = models.BooleanField(default=False)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
