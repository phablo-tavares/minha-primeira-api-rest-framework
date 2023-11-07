from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Autor, Post, Comentario
from .serializers import PostSerializer, AutorSerializer, ComentarioSerializer
from rest_framework import status
from .util import getAllInstances, getSingleInstance, createInstance, updateInstance, deleteInstance


class AutorList(APIView):

    def get(self, request):
        response = getAllInstances(
            model=Autor, serializerClass=AutorSerializer)
        return response


class AutorDetail(APIView):

    def get(self, request, pk):
        response = getSingleInstance(
            model=Autor, serializerClass=AutorSerializer, pk=pk)
        return response


class AutorCreate(APIView):

    def post(self, request):
        response = createInstance(
            model=Autor, serializerClass=AutorSerializer, data=request.data)
        return response


class AutorUpdate(APIView):

    def put(self, request, pk):
        response = updateInstance(
            model=Autor, serializerClass=AutorSerializer, pk=pk, data=request.data)
        return response


class AutorDelete(APIView):

    def delete(self, request, pk):
        response = deleteInstance(
            model=Autor, serializerClass=AutorSerializer, pk=pk)
        return response


class PostList(APIView):

    def get(self, request):
        response = getAllInstances(
            model=Post, serializerClass=PostSerializer)
        return response


class PostDetail(APIView):

    def get(self, request, pk):
        response = getSingleInstance(
            model=Post, serializerClass=PostSerializer, pk=pk)
        return response


class PostCreate(APIView):

    def post(self, request):
        response = createInstance(
            model=Post, serializerClass=PostSerializer, data=request.data)
        return response


class PostUpdate(APIView):

    def put(self, request, pk):
        response = updateInstance(
            model=Post, serializerClass=PostSerializer, pk=pk, data=request.data)
        return response


class PostDelete(APIView):

    def delete(self, request, pk):
        response = deleteInstance(
            model=Post, serializerClass=PostSerializer, pk=pk)
        return response


class ComentarioList(APIView):

    def get(self, request):
        response = getAllInstances(
            model=Comentario, serializerClass=ComentarioSerializer)
        return response


class ComentarioDetail(APIView):

    def get(self, request, pk):
        response = getSingleInstance(
            model=Comentario, serializerClass=ComentarioSerializer, pk=pk)
        return response


class ComentarioCreate(APIView):

    def post(self, request):
        response = createInstance(
            model=Comentario, serializerClass=ComentarioSerializer, data=request.data)
        return response


class ComentarioUpdate(APIView):

    def put(self, request, pk):
        response = updateInstance(
            model=Comentario, serializerClass=ComentarioSerializer, pk=pk, data=request.data)
        return response


class ComentarioDelete(APIView):

    def delete(self, request, pk):
        response = deleteInstance(
            model=Comentario, serializerClass=ComentarioSerializer, pk=pk)
        return response
