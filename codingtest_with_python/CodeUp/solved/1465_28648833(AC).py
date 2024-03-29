﻿"""
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
9 10 11 12
5 6 7 8
1 2 3 4

입력이 4 5인 경우는 다음과 같이 출력한다.
16 17 18 19 20
11 12 13 14 15
6 7 8 9 10
1 2 3 4 5

입력이 n m인 경우의 2차원 배열을 출력해보자.

입력
첫 번째 줄에 배열의 크기 n m이 입력된다.
[입력값의 정의역]
1<= n, m<= 100

출력
n*m 크기의 배열을 설명과 같이 채워 출력한다.

입력 예시   
2 3

출력 예시
4 5 6 
1 2 3 
"""

n, m = map(int,input().split())

for i in range(n,0,-1):
  for j in range(m-1,-1,-1):
    print((i*m) - j, end = ' ')
  print()
