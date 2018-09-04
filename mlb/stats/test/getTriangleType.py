# -*- coding: utf-8 -*-
# http://codingdojang.com/scode/614#answer-filter-area
# description
# [60, 60, 60] = 예각삼각형
# [30, 60, 90] = 직각삼각형
# [20, 40, 120] = 둔각삼각형
#
# [0, 90 , 90] = 삼각형이 아니다
# [60, 70, 80] = 삼각형이 아니다
# [40, 40, 50, 50] = 삼각형이 아니다
#
# 예각삼각형 : 3개의 각이 모두 예각인 삼각형
# 직각삼각형 : 1개의 각이 직각인 삼각형
# 둔각삼각형 : 1개의 각이 둔각인 삼각형
#
# ① 각이 3개가 아닐 경우 삼각형이 아니다.
# ② 3개의 각의 합이 180°가 아닐 경우 삼각형이 아니다.

arrayList = [
    [40, 40, 50, 50], [20, 40, 120], [60, 60, 60], [0, 90 , 90], [60, 70, 80], [30, 60, 90]
]
resultList = []

def getTriangleType(arrList) :
    result = None
    # if 90 in arrList : or arrList.count(90) == 1
    if arrList.count(90) == 1 :
        result = '직각삼각형'
    elif arrList[0] == arrList[1] and arrList[1] == arrList[2] :
        result = '예각삼각형'
    else :
        # 방법1
        # for idx in range(len(arrList)) :
        #     result = '둔각삼각형' if arrList[idx] > 90 else '일반삼각형'
        #     break

        # 방법2 : 삼항식 + max함수
        result = '둔각삼각형' if max(arrayList) > 90 else '일반삼각형'
    return result

for idx in range(len(arrayList)) :
    # print '길이는 : ', len(arrayList[idx])
    # print '합계는 : ', (arrayList[idx][0]+arrayList[idx][1]+arrayList[idx][2])
    # print '0도를 가지고 있나 : ', 0 not in arrayList[idx]
    # print '-------------------------------------------------'

    if len(arrayList[idx]) == 3 and sum(arrayList[idx]) == 180 and 0 not in arrayList[idx] :
        resultList.append( getTriangleType(arrayList[idx]) )
    else :
        resultList.append('삼각형이 아니무니다')

for idx in range(len(resultList)) :
    print resultList[idx]

