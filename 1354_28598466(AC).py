"""
길이 n이 입력되면 역삼각형을 출력한다.

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
"""
n = int(input())
for i in range(n,0,-1):
    print('*'*i)
    
# 중첩반복문 이용하면
"""
n = int(input())
for i in range(n,0,-1):
    for _ in range(i):
        print('*', end = '')
    print()
"""
