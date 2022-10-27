﻿"""
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
12 9 6 3
11 8 5 2
10 7 4 1

입력이 4 5인 경우는 다음과 같이 출력한다.
20 16 12 8 4
19 15 11 7 3
18 14 10 6 2
17 13 9 5 1

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
6 4 2 
5 3 1 
"""

n, m = map(int,input().split())

for i in range(n):
  for j in range(m):
    print(((n*m) - i) - (n*j), end = ' ')
  print()