﻿"""
어떤 10진수 n이 주어지면 2진수로 변환해서 출력하시오.

예)

10    ----->  1010

0    ----->  0

1    ----->  1

2    ----->  10

1024    ----->  10000000000

입력
10진수 정수 n이 입력된다.

(n은 21억이하의 임의의 수이다.)

출력
2진수로 변환해서 출력한다.

입력 예시   
7

출력 예시
111
"""
# 파이썬 내장 함수 중에 십진수 -> 이진수 변환 함수 가 있나?
n = int(input())
binary_num = ''
if n == 1 or n == 0:
    binary_num = n
else:
    while 1:
        if n == 0:
            break
        binary_num = str(n % 2) + binary_num
        n = n // 2
print(binary_num)