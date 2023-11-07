from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=500)
    autor = models.ForeignKey(
        Autor, related_name='posts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=500)
    post = models.ForeignKey(
        Post, related_name='comentarios', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.texto
