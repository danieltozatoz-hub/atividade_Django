from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    

class Tipo(models.Model):
    tipo_acervo = [('digital', 'Digital'),('físico', 'Físico')]
    
    tipo_categoria = 

    def __str__(self):
        return self.titulo