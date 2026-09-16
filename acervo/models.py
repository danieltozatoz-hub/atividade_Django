from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    

class Tipo(models.Model):
    tipo_acervo_choices = [('digital', 'Digital'),('físico', 'Físico')]
    
    categoria_choices = [('000', '000 - Generalidades e Informação'),
                      ('100', '100 - Filosofia e Psicologia'),
                      ('200', '200 - Religião e Teologia'),
                      ('300', '300 - Ciências Sociais e Direito'),
                      ('400', '400 - Linguística e Idiomas'),
                      ('500', '500 - Ciências Puras'),
                      ('600', '600 - Ciências Aplicadas'),
                      ('700', '700 - Artes e Recreação'),
                      ('800', '800 - Literatura'),
                      ('900', '900 - História e Geografia'),
    ]
    
    tipo_acervo = models.CharField(max_length=10, choices=tipo_acervo_choices)
    categoria = models.CharField(max_length=3, choices=categoria_choices)

    def __str__(self):
        return self.titulo