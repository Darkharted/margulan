from django.shortcuts import render
from rest_framework import viewsets
from masterclass.serializers import ClassSerializer
from .models import Clas
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters


class ClassViewset(viewsets.ModelViewSet):
    queryset = Clas.objects.all()
    serializer_class = ClassSerializer

    queryset = Clas.objects.all()
    # filter_backends = [
    #     filters.DjangoFilterBackend,
    #     rest_filters.SearchFilter
    # ]
    # filter_fields = ['title']
    # search_fields = ['title', 'id']