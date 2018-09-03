# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# - 리스트형 컨텐이너 타입의 데이터 반복 확장
zero_list = [0] * 100
# print zero_list
# print len(zero_list)

test_list = [ 'a','b','c','d','e','f' ]
test_list_triple = test_list * 3
# print test_list_triple --> ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']
# print "--------------------------------------"
for i, item in enumerate(test_list_triple) :
    # print i, item
    # print("{0} item of test_list: {1}".format((i + 1), [(i + 1) * e for e in item])) --> e는 제곱을 의미



