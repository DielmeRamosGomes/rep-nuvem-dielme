from django.db import models

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.DateField()
    
    def get_nome(self):
        return self.nome
    
    def get_editora(self):
        return self.editora
    
    def get_ano(self):
        return self.ano