"""
길이 n이 입력되면 다음과 같은 역삼각형을 출력한다.

예)

n이 5이면

*****
 ****
  ***
   **
    *
입력
길이 n이 입력된다.

출력
역삼각형을 출력한다.

입력 예시   
3

출력 예시
***
 **
  *
"""
n = int(input())
for i in range(n):
    print(' ' * i + '*' * (n-i))
    
# 중첩반복문 이용하면
"""
n = int(input())
for i in range(n):
    print(' ' * i, end = '')
    for j in range(n - i):
        print('*', end = '')
    print()
"""
