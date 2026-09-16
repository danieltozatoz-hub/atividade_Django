from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    

class Tipo(models.Model):
    tipo_acervo = [('digital', 'Digital'),('físico', 'Físico')]
    
    tipo_categoria = [('000', '000 - Generalidades e Informação'),
                      ('100', '100 - Filosofia e Psicologia'),
                      ('200', '200 - Religião e Teologia'),
                      ('300', '300 - Ciências Sociais e Direito'),
                      ('400', '400 - Linguística e Idiomas'),
                      ('500', ''),
                      ('700', ''),
                      ('800', ''),
                      ('900', ''),
    ]

    def __str__(self):
        return self.titulo