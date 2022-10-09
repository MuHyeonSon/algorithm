"""
출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

출력
1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

입력 예시   
10
1 3 2 2 5 6 7 4 5 9

출력 예시
1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""

n = int(input())
called_number = list(map(int,input().split()))
count_called_number = [0] * 23
for number in called_number:
    count_called_number[number-1] += 1

for count in count_called_number:
    print(count, end = ' ')
    
    
