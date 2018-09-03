# -*- coding: utf-8 -*-
# model.py의 위치를 기본에서 stats.sql.model처럼 폴더트리 구조로 간다면
# python manage.py migrate를 위해서 아래와 같이 경로를 __init__.py에서 잡아줘야 함.
from stats.sql.model import testModel