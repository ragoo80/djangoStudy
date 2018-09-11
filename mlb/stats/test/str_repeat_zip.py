# -*- coding: utf-8 -*-

# 문제
# 문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1


test_str ='aaabbcccccca'
resultStr = {}
def compress_str():
    # for s in range(len(test_str)) :
    #     if ( test_str[s] in resultStr ) :
    #         resultStr[test_str[s]] += 1
    #     else :
    #         resultStr[test_str[s]] = 1

    # for s in test_str :
    #     if ( s in resultStr ) :
    #         resultStr[s] += 1
    #     else :
    #         resultStr[s] = 1

    for s in test_str :
        resultStr[s] = resultStr[s]+1 if s in resultStr else 1

    print resultStr

    returnStr = ''
    for k, v in resultStr.items():
        returnStr += str(k)
        returnStr += str(v)
    return returnStr

# 잘못 풀었음, 내가 푼 결과값 -> a4c6b2
# 나와야 되는 결과값 -> a3b2c6a1
# print compress_str()

# 아래는 다른 사람 풀이
s = "aaaabbbcczzzza"
result = s[0]
count = 0
for i in s:
    if i == result[-1]:
        count += 1
    else:
        result += str(count) + i
        count = 1
result += str(count)
# print(result)



