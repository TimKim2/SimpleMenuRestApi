# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Menu(models.Model):
    key_name = models.CharField(max_length=30)
    store_name = models.CharField(max_length=30)
    menu_index = models.CharField(max_length=30)
    name_first = models.CharField(max_length=30)
    description_first = models.CharField(max_length=30)
    name_second = models.CharField(max_length=30)
    description_second = models.CharField(max_length=30)



# Create your models here.
