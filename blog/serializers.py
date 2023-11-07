from . import models
from rest_framework import serializers


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = [
            'id',
            'texto',
        ]


class PostSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True)

    class Meta:
        model = models.Post
        fields = [
            'id',
            'titulo',
            'conteudo',
            'comentarios',
        ]


class AutorSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = models.Autor
        fields = [
            'id',
            'nome',
            'posts',
        ]
