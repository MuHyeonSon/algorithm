# condingtest_with_python_part3_DynamicProgramming
# 편집거리.py

# 나의 풀이 (교재 해설 참고)
def thingstoedit(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)] # len(a) by len(b) size의 dp 테이블
    
    # dp 테이블 초기 설정
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    ## dp 테이블 출력
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end = " ")
        print()
        
    # dp 테이블 채워 넣기(최소 편집 거리 계산)
    for i in range(1, n + 1): 
        for j in range(1, m + 1):
            # 두 문자가 같은 경우, 왼쪽 위에 해당하는 수를 그대로 대입
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 두 문자가 다른 경우, 3가지 경우 중에서 최솟값 찾기
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    ## dp 테이블 출력
    print()
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end = " ")
        print()   
    
    return dp[n][m]

# 두 문자열 입력받기
a = input()
b = input()

# 최소 편집 거리 출력
print(thingstoedit(a, b))


# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )

def thingstoedit(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)] # len(a) by len(b) size의 dp 테이블
    
    # dp 테이블 초기 세팅
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    ## dp 테이블 출력
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end = " ")
        print()
        
    # dp 테이블 채워 넣기
    for i in range(1, n + 1): 
        for j in range(1, m + 1):
            # 두 문자가 같은 경우
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 두 문자가 다른 경우
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    
    ## dp 테이블 출력
    print()
    for i in range(n + 1):
        for j in range(m + 1):
            print(dp[i][j], end = " ")
        print()   
    
    return dp[n][m]

a = input()
b = input()

print(thingstoedit(a, b))

# 교재 풀이

# 느낀점
"""
1. 처음에 편집거리라는 문제를 제대로 생각하지 못하고 나는
LCS를 구하기 위한 DP테이블을 구현하는 프로그램을 작성해버렸다. 하지만 그마저도 i == 0인 것들과 j == 0인 위치
들의 값들에 대한 초기 세팅도 잘못하였다.

2.다시 생각해보면 문자가 같다면 아무것도 더하지 않고 그냥 현재 위치에서 왼쪽위 쪽의 값을 그대로 가져오면 되는 아이디어를 떠올렸다면
괜찮았을 텐데 그러지 못했다.

3. LCS를 구하는 DP 테이블과의 차이점은 문자가 같은 경우, 왼쪽 위값을 그대로 넣는 것, 문자가 다른 경우에는 3가지 경우에 각각 1을 더한 값들 중
가장 작은 값을 선택하여 채우는 것이다.

4. 또한 i == 0과 j==0, 두 경우 모두에 대해서 초기세팅을 0,1,2,3,,n + 1 or m + 1으로 해주어야 된다는 것을 기억해야겠다.

5.이번 문제를 통해서 LCS와 편집거리 문제의 차이를 정확히 짚고 넘어갈 수 있었고, 다음에 문제를 풀다가 만난다면,
반드시 맞출 것이다.

"""
