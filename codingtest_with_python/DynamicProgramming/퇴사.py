# condingtest_with_python_part3_DynamicProgramming
# 퇴사.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )
# N + 1일쨰 되는 날 퇴사를 한다고 했을 떄, 얻을 수 있는 최대 이익을 출력
## 내 아이디어는 순차적으로 i와 i-1번째 것을 택하여 둘 중 큰 경우를 선택하고
## 선택한 것에 해당되는 모든 날짜에 대한 이익들을 합하여 result에 저장함으로써 최종크기를 구하는 거였음.
"""
n = 7
plan = [[]]
for _ in range(n):
    plan.append(list(map(int, input().split())))

for i in range(2, n + 1):
    if plan[i][1] == 0:
        continue
    a = i - 1
    b = i
    t_a, p_a = plan[a]
    t_b, p_b = plan[b]
    profit_a = 0
    profit_b = 0
    if (a + t_a) - 1 <= (n + 1):
        for x in range(a, t_a):
            profit_a = plan[x][1]
    if (b + t_b) - 1 <= (n + 1):
        for x in range(b, t_b):
            profit_b = plan[x][1]
    if profit_a >= profit_b:
        if (a + t_a) - 1 <= (n + 1):
            for x in range(a, t_a):
                profit_a = plan[x][1]
                       
    

max_profit = 0
"""


# 교재 풀이
n = int(input()) # 전체 상담개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 각 날짜에서 마지막날까지 받을 수 있는 최대 금액을 각각 저장하기위한 dp테이블
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    
# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n: #####??? n이면 벗어나는 거 아니야?
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value
    print(f'i : {i}, time : {time}, dp[{i}] : {dp[i]}, max_value : {max_value}, dp : {dp}')
print(dp[0])




# 느낀점
"""
1. 뒤쪽에서부터 거꾸로 확인하는 방식으로 푸는 것에 대한 확신을 갖기 어려웠고,

2. 어떤 문제에서 뒤쪽부터 계산하는 것이 좋은지 특징을 정확히 파악하지 못하여서, 해설을 보고난 뒤에도 어렵다.

3. DP를 많이 풀어보면서 익숙해진다면 해당문제와 같은 문제를 실전에서 주어졌을 때, 풀 수 있을까

4. 교재 풀이의 인덱스를 다루는 것도 굉장히 이해하는데 오래걸려서, 더 자세한 설명이 있었으면 좋겠다고 생각했다.

5. 지금 시점에서 문제를 100프로 이해하지 못했기 때문에, 해당 문제에 대한 글을 올리기는 아직 이른 것 같다.
"""
