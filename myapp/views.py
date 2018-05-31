# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from .serializers import PersonSerializer
from myapp.models import Person
from myapp.models import Menu
from .serializers import MenuSerializer
from rest_framework import filters


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name']


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['key_name']


class FindMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
