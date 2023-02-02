# condingtest_with_python_part3_DynamicProgramming
# 금광.py

# 나의 풀이 (교재 해설 참고)
"""
def search(dp):
    # 왼쪽 위, 왼쪽, 왼쪽 아래에서 오는 경우를 모두 고려하여 그 중 최댓값으로 갱신
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1] 
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
     

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(list(data[index : index + m]))
        index += m  
    
    search(dp)

"""

# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )

"""
t = int(input())
n, m = map(int, input().split())

def search(dp):
    dptable = []
    dptable[
        

for i in range(t):
    data = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(list(data[index : index + m]))
        index += m   
    search(dp)
"""
# 두 번째 품
## 올 수 있는 경우는 세가지(왼쪽 위, 왼쪽 왼쪽 아래) 이 세가지 중 가장 큰 걸 더하면 되고, 인덱스 초과하는 경우를 처리
## 해주면 됨
def search_max(dp):
    for j in range(1, m):
        for i in range(n):
            # 만약 왼쪽 위가 없다면
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            
            left = dp[i][j - 1]
            
            # 만약 왼쪽 아래가 없다면
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)      
    
    max_value = 0
    for i in range(n):
        max_value = max(max_value, dp[i][m - 1])
    
    return max_value    

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split())) 
    dp = [] 
    for i in range(len(temp)//m):
        dp.append(temp[i*m:(i+1)*m])    
    
    print(search_max(dp))
    
# 교재 풀이


# 느낀점
"""
dp table이 꼭 1차원으로만 만드는게 아니라 2차원으로 만들고, 그 테이블에서 최댓값 찾아도 된다는 것을
생각해낼 수 있었다..

정수 삼각형 문제 풀고 다시 2번째 풀면서 느낀점
1. 입력받은 1줄에 금광정보를 n x m 형태로 만들 때 매우 비효율적으로 작성했고, for문도 n번 돌리면 되는 것을
    길이를 구해서 나누는식으로 엄청 복잡하게 작성했음을 알 수 있었다.
"""
