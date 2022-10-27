﻿"""

이번엔 마름모를 출력해보자. 

n이 입력되면 대각선 2개의 길이가 2n인 마름모를 출력하시오.

입력
정수 n이 입력된다. ( 2 <= n <= 100 )

출력
대각선 2개의 길이가 2n인 마름모를 출력한다.

입력 예시   
5

출력 예시
    **
   *  *
  *    *
 *      *
*        *
*        *
 *      *
  *    *
   *  *
    **

"""
n = int(input())

for i in range(n*2):
  if i < n :
    print(' ' * ((n-1) - i) + '*' + ' ' * (i * 2) +  '*')
  elif i >= n :
    print(' ' * (i - n) + '*' + ' ' * (((n*2)-2) - (2*(i - n))) +  '*')