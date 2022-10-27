﻿"""
철수는 인쇄소에서 근무하고 있다. 인쇄소의 주된 업무는 종이에 문자와 그림을 인쇄하는 것이다. 종이의 종류는 다양하고, 고객마다 요구하는 종이의 크기도 다양하다.

 

인쇄소에는 종이를 크기에 따라 자동으로 잘라주는 최신식 인쇄기가 있다. 그런데 어느 날 기계가 고장이 난 상태에서 인쇄를 요구하는 고객이 찾아왔고, 마침 그 고객이 요구하는 크기의 종이도 없어 큰 종이를 수동으로 잘라야 하는 상황이 되었다.

 

철수는 종이를 고객이 요구하는 크기대로 잘라보려고 했으나, 절취선이 없어 쉽지 않았다.

 

고객이 요구하는 가로, 세로 길이가 주어지면 아주 큰 종이에 다음과 같은 절취선을 그리는 프로그램을 작성하시오.

 

예를 들어 12*4의 종이라면,

+----------+

|          |

|          |

+----------+

를 출력한다.

입력
가로 길이 n과 세로 길이 m이 공백으로 분리되어 입력된다.(2 <= n, m <= 50)

 

출력
n*m 크기의 종이를 출력한다.

가로는 '-', 세로는 '|'로 출력하며, 가로와 세로가 겹치는 부분은 '+'로 출력한다.

입력 예시   
4 3

출력 예시
+--+
|  |
+--+
"""

n,m = map(int,input().split())
for i in range(1,m+1):
  if i== 1 or i == m:
    print('+' + '-' * (n-2) + '+')
  else:
    print('|' + ' ' * (n-2) + '|') 

"""
# 중첩반복문 이용
for i in range(1,m+1):
  for j in range(1,n+1):
    if (i== 1 or i == m) and (j == 1 or j == n) :
      print('+', end = '')
    elif (i== 1 or i == m):
      print('-', end = '')
    elif(j== 1 or i == n or j == n):
      print('|', end = '')
    else:
      print(' ', end = '')
"""