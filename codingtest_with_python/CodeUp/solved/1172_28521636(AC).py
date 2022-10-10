"""
세 정수가 입력된다.

출력
낮은 숫자 부터 출력한다.

입력 예시   
8 7 6

출력 예시
6 7 8
"""
a = list(map(int,input().split()))
a.sort()
for x in a:
    print(x, end = ' ')
