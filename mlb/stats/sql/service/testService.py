# -*- coding: utf-8 -*-

# from stats.sql.mapper.testMapper import TestMapper -> class로 되어 있을때

from stats.sql.mapper import testMapper

def insertPlayer():
    testMapper.DB_connect('create_db_exec')
    # testMapper.getCursor()


