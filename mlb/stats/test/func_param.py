# -*- coding: utf-8 -*-
# positional arguments, keyword arguments

def save_ranking(first, second, third=None, fourth=None) :
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print (rank)

# save_ranking('ming', 'alice')
# save_ranking('alice', 'ming', third='mike')
# save_ranking('alice', 'ming', 'mike', fourth='jim')




# def function(*args, **kwargs):
# --> keyword는 position 보다 앞에 나올 수 없음.
# *positionArgs, **keywordArgs --> arguments 이름을 원하는 데로 변경하여 사용가능
def position_ranking(*args, **kwargs):
    print(args)
    print(kwargs)
# position_ranking('ming', 'alice', 'tom', fourth='wilson', fifth='roy')
# ('ming', 'alice', 'tom') --> get return tuple type
# {'fourth': 'wilson', 'fifth': 'roy'} --> get return dict type


from functools import reduce
primes  = [2,3,5,7,11,13]

def product(*numbers) :
    p = reduce(lambda x, y : x*y, numbers)
    print 'input' , p

product(*primes)
product(primes)