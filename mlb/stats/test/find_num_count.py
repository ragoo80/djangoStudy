# -*- coding: utf-8 -*-

# 문제
# 1~1000에서 각 숫자의 개수 구하기

# 예시
# 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5
# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개


# 한자리수 1~9			-> 1번씩 추가
# 두자리수 10 ~ 19		-> (10^n)*num_type_len 추가
# 세자리수 100 ~ 199	    -> (100^n)*num_type_len 추가
# 네자리수 1000 -> 0:3, 1:1

# 쓸 수 있는 숫자 개수
num_type_len = 10
result_num_obj = {
    '0' : 0,
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0
}

def setCount( addCount ) :
    for idx in range(len(result_num_obj)) :
        # print result_num_obj[str(idx)]
        result_num_obj[str(idx)] += addCount

# setCount( 1 )
# setCount( (10**2)*num_type_len )
# setCount( (100**2)*num_type_len )
# result_num_obj['0'] += 3
# result_num_obj['1'] += 1
#
# for idx in range(len(result_num_obj)) :
#     print 'key : ', idx, ' and value : ', result_num_obj[str(idx)]



# 다른 사람들 정답
# count={ x:0 for x in range(0,10) }
# for x in range(1,1001):
#     for i in str(x):
#         count[int(i)]+=1
# print(count)

#정의된 문자열(String)에서 해당문자가 몇번 존재하는지 카운트하는 방법입니다.
# for x in range(10):
#     print( '%d: %d' %( x,''.join(map(str, range(1, 1001))).count(str(x)) ))




