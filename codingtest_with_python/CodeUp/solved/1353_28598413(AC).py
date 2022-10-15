"""
n이 입력되면 다음과 같은 삼각형을 출력하시오.

예)

n 이 5 이면

*
**
***
****
*****
입력
길이 n이 입력된다.

출력
삼각형을 출력한다.

입력 예시   
3

출력 예시
*
**
***
"""
# 첫 번째줄은 하나 두 번째줄은 두 개 세 번째 줄은 셋
n = int(input())
for i in range(n):
    for _ in range(i+1):
        print('*', end = '')
    print()
    
# 중첩 반복문 말고 더 간단하게
"""
n= int(input())
for i in range(n):
    print('*'*(i+1))
"""

