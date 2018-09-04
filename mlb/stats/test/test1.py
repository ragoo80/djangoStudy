# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


# a = 2
# def test():
#     print("inside test", a)
#     a = 3
#
# test()
# print("after test", a)



# to find value in list test ------------------------------------------------------------
StrList = ['x','t','ab','ssd']
# print StrList.index('t')
# print StrList.index('tsd') --> ValueError: u'tsd' is not in list

NumList = [33,55,15,125,36254]
result = NumList.index(55) if 55 in NumList else 'there is not 33'


# using for lambda function ------------------------------------------------------------
# 람다는 한 줄로 함수를 작성하는 방법인데 식 형태로 되어 있다고 해서 람다 표현식(lambda expression)이라고 부른다.
# 람다는 함수를 간편하게 작성할 수 있어서 다른 함수의 인수로 넣을 때 주로 사용.

# 람다 적용 전
def plusFn(x) :
    return x + 10
# result = list( map(plusFn, [1,2,3]) )

# 람다로 적용 후
result = map( lambda x: x+10, [1,2,3] )


# to find an element in a string array use ------------------------------------------------------------
# case by use lamda expression code
strlist = ["Moon","Earth","Jupiter","Neptune","Earth","Venus"]
get_indexes = lambda target, list: [index for (value, index) in zip(list, range(len(list))) if target == value]
# print(get_indexes("Earth",strlist))

# case by just use normal function expression code
# strlist = ["Moon","Earth","Jupiter","Neptune","Earth","Venus"]
# def testFn(target, list) :
#     for (y, i) in zip( list, range(len(list)) ) :
#         # print zip( list, range(len(list)) )
#         # print 'y is : ', y , 'and i is : ', i
#     return [ index for (value, index) in zip( list, range(len(list)) ) if target == value ]
# testFn("Earth",strlist)

# example any,all function ------------------------------------------------------------
# any 함수는 Iteration 이 가능한 객체를 받아 그 항목을 돌면서 어느 하나라도 True 이면 결과로 True를 리턴
# print any([False, False, False])    # False
# print any([False, True, False])     # True
# 반면 all 함수는 리스트의 모두가 True일 경우만 True
# print all([False, True, False])    # False
# print all([True, True, True])    # True

# test max function by tuple ------------------------------------------------------------
tupleList = (33,55,66)
print max(tupleList)