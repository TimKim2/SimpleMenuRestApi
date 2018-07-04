# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets
from data.models import Store
from rest_framework import filters
from django.core.cache import cache
from .serializers import StoreSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ['key_number']




