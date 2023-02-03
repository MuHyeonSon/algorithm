# condingtest_with_python_part3_DynamicProgramming
# 병사배치하기.py

# 나의 풀이 (교재 해설 참고)
"""
n = int(input()) # 병사의 수

# 병사들의 전투력 입력받기
power = list(map(int, input().split()))
dp = [1] * n
power.reverse()
print(power)

for i in range(1, n):
    for j in range(0, i):
        if power[i] > power[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(n - max(dp))
"""
# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 분 초 )
## 단순히 남아있는 병사들의 수가 최대가 되도록 열외를 시키는 거임
## 열외를 시키는 이유는 내림차순이 되도록 하기 위해서임
## 열외시켜야되는 병사의 수 출력하기

## 0번 부터 n-1번까지 한 명씩 뺴는 경우를 모두 구해보고 가장 작은 경우를 선택하면 되지 않을까??
## i번을 뺴면 경우에 따라 남은 병사들 중에 뺴야될 애들이 바뀔 수 있을 거고, 그러면 열외시키는 병사의 수도 달라질 수 있을테니

## 아니면 이 문제도 뒤에서 부터 확인 해야 되나??
"""
from copy import deepcopy

def check(array):
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            return False
    return True

n = int(input()) # 병사의 수

# 병사들의 전투력 입력받기
power = list(map(int, input().split()))
dp = [0] * n

if check(power) == True:
    print(0)
else:
    for i in range(n):
        if check(power) == True:
            break
        temp = deepcopy(power)
        #print(f'temp : {temp}')
        temp.pop(i)
        #print(f'temp : {temp}')
        #print(f'power : {power}')
        count = 1
        for j in range(1, n-1):
            if temp[j - 1] < temp[j]:
                count += 1
        dp[i] = count

    print(min(dp))

print(f'dp : {dp}')
"""

# 교재 풀이
n = int(input())
array = list(map(int, input().split()))
## 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

## DP를 위한 1차원 DP테이블 초기화 
dp = [1] * n 

## LIS 수행
for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            dp = max(dp[i], dp[j] + 1)
## 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))
            

# 느낀점
"""
1. 해설을 확인하기 전까지는 LIS라는 것을 알아차리지 못했고,
2. 전형적인 LIS문제로 반드시 코드와 동작원리를 숙지하고 있어야겠다고 생각했다.
"""
