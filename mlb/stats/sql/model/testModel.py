# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


# ----------------------------------------------------------------------------------------------------
# 마이그레이션 파일 생성
# $ python manage.py makemigrations <app-name>
# 마이그레이션 적용
# $ python manage.py migrate <app-name>
# 마이그레이션 적용 현황
# $ python manage.py showmigrations <app-name>
# 지정 마이그레이션의 SQL 내역
# python manage.py sqlmigrate <app-name> <migration-name>
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# class Player(models.Model) :
#     name = models.CharField(max_length=20)
#     birth = models.DateTimeField('date published')
#     age = models.IntegerField()
#
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#
#
# class testAdd(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
# ----------------------------------------------------------------------------------------------------


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now )
    published_date = models.DateTimeField( blank=True, null=True )

    # 해당 레코드 생성시 현재 시간 자동저장
    # created_at = models.DateTimeField(auto_now_add=True)
    # 해당 레코드 갱신시 현재 시간 자동저장
    # updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title