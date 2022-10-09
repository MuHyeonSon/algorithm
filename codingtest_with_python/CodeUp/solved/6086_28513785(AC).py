"""
1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
그때까지의 합을 출력한다.

입력 예시   
57

출력 예시
66
"""
n = int(input())
sum = 0
s = 1

while 1:
    sum = sum + s
    s += 1
    if sum >= n:
        print(sum)
        break

