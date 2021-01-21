from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.


class Artigo(models.Model):
    nome = models.CharField(max_length=192)
    foto = CloudinaryField('portifolio', null=True, blank=True)
    conteudo = RichTextField()

    def __str__(self):
        return f"{self.nome}"


class Projeto(models.Model):
    nome = models.CharField(max_length=32)
    foto = CloudinaryField('portifolio')
    descricao = RichTextField()
    url = models.URLField()

    def __str__(self):
        return f"{self.nome}"