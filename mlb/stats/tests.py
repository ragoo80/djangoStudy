# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import os


# Create your tests here.

# db연결 test
# from sql.service import testService
# testService.insertPlayer()

# 경로 test
# from mlb.settings import BASE_DIR
# print BASE_DIR
# testpath = os.path.join( BASE_DIR, 'stats/tf' )
# print 'testpath : ' + testpath
# print 'absPath : ', os.path.abspath(testpath)
# README = open( os.path.join(os.path.dirname(__file__), 'README.rst') ).read() -> sampleCode


# check admin user list
# import django
# import os
# from django.contrib.auth import get_user_model
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlb.settings")
# django.setup()
#
# user = get_user_model()
# print user.objects.all()


#add admin Post test in terminal python manage.py shell
# list = Post.objects.all()
# userList = User.objects.all()
# adminUser = User.objects.get(username='root')
# Post.objects.create(author=adminUser, title='ragoo add post test', text='is all right?')

# from django.utils import timezone
# Post.objects.filter(author=me)
# Post.objects.filter(title__contains='Koala')
# Post.objects.filter(published_date__lte=timezone.now())
# post = Post.objects.get(title__contains="Goodbye")
# post.publish()
# Post.objects.filter(published_date__lte=timezone.now())

# Post.objects.order_by('created_date')
# Post.objects.order_by('-created_date')
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')