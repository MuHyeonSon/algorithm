# condingtest_with_python_part2_다이나믹_프로그래밍
# 피보나치수열(반복문).py

# 나의 풀이

# 나의 풀이 (Product Code)

# 교재 풀이

## DP Table (앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화)
d = [0] * 100 # 99까지 구하려면 0 포함하니까 100이어야 됨)

# 첫 번째, 두 번째, 원소는 1
d[1] = 1
d[2] = 2
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2]

print(d[n])

# 느낀점
"""

"""
