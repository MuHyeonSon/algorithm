# 369 게임
"""
9

출력 예시
1 2 X 4 5 X 7 8 X
"""

n = int(input())

for i in range(1,n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i) :
        print('X', end = ' ')
    else:
        print(i, end = ' ')
