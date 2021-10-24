from django.db import models

# Create your models here.



class Projetos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.descricao


