﻿"""
1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
3의 배수는 출력하지 않는다.

입력 예시   
10

출력 예시
1 2 4 5 7 8 10
"""

n = int(input())
for i in range(1,n+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end = ' ')