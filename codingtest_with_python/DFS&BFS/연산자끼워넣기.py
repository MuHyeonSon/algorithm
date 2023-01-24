# condingtest_with_python_part3_DFS/BFS
# 연산자끼워넣기.py

# 나의 풀이 (교재 해설 참고) itertools 사용
from itertools import product
from itertools import permutations

n = int(input())

## n개의 수 입력받기
numbers = list(map(int, input().split()))

## +의 개수, -의 개수, 곱셈의 개수, 나눗셈(//)의 갯수 입력받기
number_operations = list(map(int, input().split()))

operations = []
result = []

for i in range(4):
    if i == 0:
        for j in range(number_operations[i]):
            operations.append('+')
    elif i == 1:
        for j in range(number_operations[i]):
            operations.append('-')
    elif i == 2:
        for j in range(number_operations[i]):
            operations.append('*')
    elif i == 3:
        for j in range(number_operations[i]):
            operations.append('//')        
            
candidates = list(permutations(operations, n - 1))
#candidates = list(product(['+', '-', '*', '//'], repeat = (n-1)))
#print(f'candidates : {candidates}')
#print(f'operations : {operations}')

value = 0
for candidate in candidates:
    for i in range(n):
        if i == 0:
            value = numbers[i]
        else:
            if candidate[i-1] == '+':
                value += numbers[i]
            elif candidate[i-1] == '-':
                value -= numbers[i]
            elif candidate[i-1] == '*':
                value *= numbers[i]
            elif candidate[i-1] == '//':
                value = int(value / numbers[i])
                #value = value // numbers[i]
    result.append(value)
    
print(max(result))
print(min(result))

# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )

## n개의 수(1<= 주어지는 숫자들 <= 100)와 n-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구해라
## 이건 왜 DFS BFS문제일까 이것도 재귀로 구현해야돼서 일까..

## 최댓값 만들기
## 만약 1보다 같거나 작으면 더하기를 하고, 1보다 크면 곱하기를 하는게 최대로 크게 만들 수 있다.
## 그리고 나누기가 존재한다면 빼기 다하고 나서 숫자로만 사용
## 빼기는 가장 작은 숫자로 사용 

## 최솟값 만들기
## 뺼샘사용할 수 있으면 무조건 뺼썜먼저 다사용
## 

## 아니 연산자를 끼워 넣는거야.. 
"""
n = int(input())

## n개의 수 입력받기
numbers = list(map(int, input().split()))

## +의 개수, -의 개수, 곱셈의 개수, 나눗셈(//)의 갯수 입력받기
operations = list(map(int, input().split()))

result = []
max_value = 0
min_value = 0


# 최솟값 찾기
for i in range(n):
    if i == 0:
        min_value = numbers[i]
    # 현재 양수라면
    if min_value >= 0:
        # 뺼쌤 연산 가능하면
        if operations[1] > 0:
            min_value -= numbers[i]
            operations[1] -= 1
        # 나눗셈 연산 가능하면
        elif operations[3] > 0:
            min_value //= numbers[i]
            operations[3] -= 1
        # 더하기 연산 가능하면
        elif operations[0] > 0:
            min_value += numbers[i]
            operations[0] -= 1
       # 곱하기 연산 가능하면
        elif operations[2] > 0:
            min_value *= numbers[i]
            operations[2] -= 1
    # 현재 음수라면
    else:
       # 곱하기 연산 가능하면
        if operations[2] > 0:
            min_value *= numbers[i]
            operations[2] -= 1        
        # 뺼쌤 연산 가능하면
        elif operations[1] > 0:
            min_value -= numbers[i]
            operations[1] -= 1
        elif (min_value // numbers[i]) <= (min_value + numbers[i]):
            # 나눗셈 연산 가능하면
            if operations[3] > 0:
                min_value //= numbers[i]
                operations[3] -= 1
            # 더하기 연산 가능하면
            elif operations[0] > 0:
                min_value += numbers[i]
                operations[0] -= 1
        elif (min_value // numbers[i]) > (min_value + numbers[i]):
            # 더하기 연산 가능하면
            if operations[0] > 0:
                min_value += numbers[i]
                operations[0] -= 1            
            # 나눗셈 연산 가능하면
            elif operations[3] > 0:
                min_value //= numbers[i]
                operations[3] -= 1

# 최댓값 찾기
for i in range(n):
    if i == 0:
        max_value = numbers[i]
    # 현재 양수라면
    if max_value >= 0:
        # 나눗셈 연산 가능하면
        if operations[3] > 0:
            max_value //= numbers[i]
            operations[3] -= 1
        # 더하기 연산 가능하면
        elif operations[0] > 0:
            max_value += numbers[i]
            operations[0] -= 1
        # 곱하기 연산 가능하면
        elif operations[2] > 0:
            max_value *= numbers[i]
            operations[2] -= 1
        # 뺼쌤 연산 가능하면
        elif operations[1] > 0:
            max_value -= numbers[i]
            operations[1] -= 1
    # 현재 음수라면
    else:
        # 더하기 연산 가능하면
        if operations[0] > 0:
            max_value += numbers[i]
            operations[0] -= 1
        # 나눗셈 연산 가능하면
        if operations[3] > 0:
            max_value //= numbers[i]
            operations[3] -= 1
       # 곱하기 연산 가능하면
        if operations[2] > 0:
            max_value *= numbers[i]
            operations[2] -= 1        
        # 뺼쌤 연산 가능하면
        elif operations[1] > 0:
            max_value -= numbers[i]
            operations[1] -= 1
            
        elif (max_value - numbers[i]) <= (max_value * numbers[i]):
            # 곱하기 연산 가능하면
            if operations[2] > 0:
                max_value *= numbers[i]
                operations[2] -= 1
            # 빼기 연산 가능하면
            elif operations[1] > 0:
                max_value -= numbers[i]
                operations[1] -= 1
        elif (max_value - numbers[i]) > (max_value * numbers[i]):
            # 빼기 연산 가능하면
            if operations[1] > 0:
                max_value -= numbers[i]
                operations[1] -= 1            
            # 곱하기 연산 가능하면
            elif operations[2] > 0:
                max_value *= numbers[i]
                operations[2] -= 1
                
# 최댓값 출력
print(max_value)

# 최솟값 출력
print(min_value)

"""

# 교재 풀이 dfs

n = int(input())
## 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
## 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

## 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

## 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1
            
# DFS 메서드 호출
dfs(1, data[0])

print(max_value)
print(min_value)
            


# 느낀점
"""
우선 무조건 기억해야될 점은 다음과 같다.

1. 아래 두 가지 식의 결과값은 서로 다르다(여러 가지 경우 시도해본 결과 음수가 들어있을 때 결과가 달랐음).

value = int(value / numbers[i])
value = value // number[i]

2. 재귀함수 구현 시 모든 경우의 수를 다 따질 때와 같이 함수 자체를 여러번 사용할 떄?? 
    정확히 정의하기는 어렵지만 카운트를 하고, dfs함수를 재귀적으로 수행한다면 수행 후 다시 카운트 변수를 원상복구 한다.
"""
