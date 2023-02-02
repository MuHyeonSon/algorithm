# condingtest_with_python_part3_DynamicProgramming
# 정수삼각형.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )
## 아래 층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있음.
## 금광문제와 매우 비슷한 것 같은데.. 기억이 희미함
## 금광문제보다 좀 더 업그레이드된 문제임 왜냐면 직사각형 테이블 모양이 아니고, column 수도 늘어남
## 금광문제처럼 특정 위치에서는 특정 조건을 거르는 식으로 조건문 구현해서 DP 테이블에 저장해야됨
## 금광에서는 리스트 하나만 써서 금광리스트에서 바로 값을 갱신하면서 DP테이블로서 사용했음.
## 잠시만
## 대각선 왼쪽과 대각선 오른쪽은 바로 그 위층의 i번쨰와 i번쨰 + 1임
## 갱신할 때는 이전값과 현재값 둘 중의 max값으로 갱신하면 될 듯.

## 삼각형의 크기 입력 받기
"""
from copy import deepcopy

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = deepcopy(array)

for i in range(n-1): # 각 층의 원소의 개수와 i가 일치
    for j in range(i + 1): # i층 바로 밑에 층에 인덱스에 접근
        #print(f'dp[{i+1}][{j}] : {max(dp[i+1][j], dp[i+1][j] + dp[i][j])}')
        #print(f'dp[{i+1}][{j + 1}] : {max(dp[i+1][j + 1], dp[i+1][j + 1] + dp[i][j])}')
        #print(dp)
        #print("--------------------------------------------------------")
        dp[i + 1][j] = max(dp[i + 1][j], array[i + 1][j] + array[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], array[i + 1][j + 1] + array[i][j])
    for j in range(i + 1):
        array[i + 1][j] = dp[i + 1][j]
        array[i + 1][j + 1] = dp[i + 1][j + 1] 
    #print(f'array : {array}')   
## 지금의 상태는 단순히 max값만을 찾은 거임 그니까 그러면 안되고

#max_value = 0
#for floor in dp:
#    max_value = max(floor)
print(dp)
print(max(dp[n - 1]))

"""
# 교재 풀이

n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

## 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인 
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        # 만약 j == 0이라 왼쪽 위가 없는 경우에는
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 만약 j == i라 바로 위가 없는 경우에는
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 왼쪽 위, 바로 위 둘 중에 더 큰 값을 더해서 저장 (최대합을 저장)
        dp[i][j] = dp[i][j] + max(up_left, up)                

print(max(dp[-1]))

# 느낀점
"""
1. 완전히 비효울적이고, 교재해설과 비교했을 때 이상하게 풀었다.

2. 내려올 수 있는 경우가 2가지이면 그 2가지 중에 더 큰걸 선택하여 더하면 되는 것인데,
    나는 일단 더하고 저장한뒤, 다음 차례 떄 그 값보다 지금 경우에서 더한 값이 더크다면 지금 더한 값으로
    바꾸는 식으로 구현해서, 중간에 값이 덮어씌워져 원하는 결과가 안나오게끔 된 것였고
    이것을 2차원 리스트에 삼각형정보하나를 그대로 초기에 복사해놓아서 리스트를 하나 더사용했음,
    하지만 교재에서는 리스트 하나만 사용했고, 실제로 그렇게 풀 수 있는 문제였음.

3. 그래도 답이 나오게끔 작성하기는 했고, 교재풀이를 잘 기억하고 비슷한 문제가 나왔을 때,
    교재풀이 방법을 이용해서 더 간단하게 코드를 작성해서 해결할 수 있고 그렇게 해야겠다고 생각했다. 
"""
