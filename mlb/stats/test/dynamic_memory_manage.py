# -*- coding: utf-8 -*-

# 전제 조건
# 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 입력받은 정수의 개수만큼 정수를 입력받는다.
# 입력받은 정수의 합과 평균 값을 출력한다.
# 할당된 메모리공간을 비운다.

# 요구사항
# 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 사용한 공간은 마지막에 비워야 한다.
# 배열을 사용하면 안된다.


from __future__ import unicode_literals


class dynamic_memory_manage(object):
    """docstring for dynamic_memory_manage"""
    def __init__(self, arg):
        super(dynamic_memory_manage, self).__init__()
        self.arg = arg



def main() :
    '''in python 2.7 version use raw_input()'''
    ea = input("입력할 정수 n개를 입력해 주세요 : ")
    integers = input("정수를 입력해 주세요 : ").split(',')
    sum = 0

    # for index in range(len(integers)):
    for value in integers:
        sum += int(value)

    avg = float(sum/int(ea))
    print (sum, avg)
    print ("입력 총합은 : %d" %sum )
    print ("입력 평균은 : %f" %avg )

    del ea, integers, sum, avg

if __name__ == '__main__':
    main()