﻿"""
하나의 정수 N을 입력받아 다음과 같이 지그재그로 출력하시오.

N이 3이라면,

1 6 7

2 5 8

3 4 9

입력
정수 n이 입력된다. ( 1 <= n <= 100)

출력
n * n 배열을 수직으로 채워서 출력한다.

입력 예시   
3

출력 예시
1 6 7 
2 5 8 
3 4 9 
"""

N = int(input())

for i in range(1,N+1):
  for j in range(1,N+1):
    if j % 2 == 0: # 짝수번째 열이라면
      print((N*j) - (i-1),end = ' ') # 내림차순
    else: # 홀수번째 열이라면
      print(N*j - (N-i),end = ' ') # 오름차순
  print()