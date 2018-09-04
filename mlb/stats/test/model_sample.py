# -*- coding: utf-8 -*-

# Django Annotation/Aggregation
# http://raccoonyy.github.io/django-annotate-and-aggregate-like-as-excel/

from __future__ import unicode_literals
from django.test import TestCase

from django.db.models import F, Sum, Count, Case, When

# Implements django model
class Product(models.Model) :
    name = models.CharField('이름', max_length=100, unique=True)
    price = models.IntegerField('가격')

# 판매내역
class OrderLog(models.Model) :
    product = models.ForeignKey('Product')
    created = models.DateTimeField(u'판매일')

# 제품별 가격 참조하기(values) - excel version --> static/images/saleList.png 참조
order_qs = OrderLog.objects.values( 'created', 'product__name', 'product__price' )
# order_queryset의 내용을 출력해보면 엑셀과 같음을 알 수 있습니다.
# for order in order_qs :
#     print(order)
# >>> {'product__price': 9900, 'created': datetime.datetime(2016, 4, 1, 0, 0), 'product__name': 'ABC Activity'}


order_qs = OrderLog.objects.annotate(
    name=F('product__name'),
    price=F('product__price')
).values( 'created', 'name', 'price' )
# >>> {'price': 9900, 'created': datetime.datetime(2016, 4, 1, 0, 0), 'name': 'ABC Activity'}


# Django에서 querySet의 특정 필드를 모두 더 할때는 aggregate 메서드 사용, 합이나 평균, 개수 등을 계산할 때 사용
# >>> order_qs.aggregate(total_price=Sum('price'))    >>>     {'total_price': 262200}