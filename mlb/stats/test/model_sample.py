# -*- coding: utf-8 -*-

# Django Annotation/Aggregation
# http://raccoonyy.github.io/django-annotate-and-aggregate-like-as-excel/

from __future__ import unicode_literals
from django.test import TestCase

from django.db.models import F, Sum, Count, Case, When












# ----------------------------   판매 내역 구하기 test   -------------------------------------------

# Implements django model
class Product(models.Model) :
    name = models.CharField('이름', max_length=100, unique=True)
    price = models.IntegerField('가격')

# 판매내역
class OrderLog(models.Model) :
    product = models.ForeignKey('Product')
    created = models.DateTimeField(u'판매일')

