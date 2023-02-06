# condingtest_with_python_part3_DynamicProgramming
# 편집거리.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )

def thingstoedit(a, b):
    n = len(a)
    m = len(b)
    dp = [[1] * (m + 1) for _ in range(n + 1)] # len(a) by len(b) size의 dp 테이블
    for i in range(1, n): 
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
a = input()
b = input()

print(thingstoedit(a, b))

# 교재 풀이

# 느낀점
"""
"""

"""
📰 Codingtest_with_python_part3_DynamicProgramming
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 DynamicProgramming 문제 풀이 느낀점
"""





def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i #첫행 초기화
    for j in range(1, m + 1):
        dp[0][j] = j #첫열 초기화

    for i in range(1, n + 1):
        for j in range(1, m + 1):
     #문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
     #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: #삽입(왼쪽), 삭제(위쪽), 교체 (왼쪽 위) 중에서 최소 비용
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    for i in dp:
        for j in i:
            print(j, end=" ")
        print("")
    return dp[n][m]

str1 = 'cat'
str2 = 'cut'

print(edit_dist(str1, str2))
