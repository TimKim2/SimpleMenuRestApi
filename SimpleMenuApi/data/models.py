# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Store(models.Model):
    key_number = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    menu = models.CharField(max_length=500)

#{menuname, price, description}

