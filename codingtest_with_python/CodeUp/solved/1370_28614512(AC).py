﻿"""

높이 h와 반복휫수 r이 주어질때, 별을 다음과 같이 지그재그로 출력하자.

예) 3 2

*
 *
  *
 *
*
*
 *
  *
 *
*
입력
높이 h과 반복횟수 r가 한줄에 주어진다.(1<= h, r<=40)

출력
지그재그로 출력한 모습을 출력한다.

입력 예시   
3 3

출력 예시
*
 *
  *
 *
*
*
 *
  *
 *
*
*
 *
  *
 *
*

"""

h, r = map(int,input().split())

for i in range(r):
  for i in range((h*2) - 1):
    if (i+1) <= h:
      print(' ' * i + '*')
    elif (i+1) > h:
      print(' ' * ((h-1) - (i - (h-1))) + '*')

