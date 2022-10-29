# condingtest_with_python_part2_greedy
# greedy_1이될때까지.py

# 과정 1. N에서 1을 뺀다.
# 과정 2. N을 K로 나눈다.

# 나의 풀이
N, K = map(int,input().split())

count = 0

while 1:
  if N % K == 0:
    N //= K
    count += 1
  else:
    N -= 1
    count += 1
  # 연산 후 결과 N이 1이라면 반복문 빠져나감
  if N == 1:
    break

print(count) # 과정 1,2 총 실행 횟수의 최솟값 출력

# 교재 풀이 (단순하게 푸는 답안 예시)
n, k = map(int,input().split())
result = 0

# n이 k이상이라면 k로 계속 나누기
while n >= k:
  # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
  while n % k != 0:
    n -= 1
    result += 1

  n //= k
  result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
  n -= 1
  result += 1

print(result)

# 교재 풀이 (N이 100억 이상의 큰 수가 되는 경우-> N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식)
n, k = map(int,input().split())
result = 0

# n이 k이상이라면 k로 계속 나누기
while True:
  # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  while n % k != 0:
    n -= 1
    result += 1

  n //= k
  result += 1

while True:
  # (N == K로 나누어떨어지는 수)가 될때까지 1씩 빼기
  target = (n // k) * k  # 나누어 떨어지는 가장가까운 수를 저장
  result += (n - target) # 나눌 수 있는 수가 될 때까지 빼는 횟수 더하기
  n = target # 나누어떨어지는 수 중 가장 가까운수를 n 으로 업데이트
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k :
    break
  # k로 나누기
  result += 1 # 나누기 연산에 대한 횟수 더하기
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기

result += (n-1)
print(result)

# 느낀점 
# 교재풀이 1을 보고 굳이 저렇게 짜는 이유가 있을까라는 생각을 했다.
# 비교연산을 하는데 있어서 내가 짠 코드와 교재풀이1은 결국 반복문 한 번마다
# 비교연산 2회를 하기 때문에 같을 텐데 풀이 방식을 좀 더 잘 이해가가도록 표현한 것은
# 교재풀이가 더 그러하다고 생각했고 교재풀이 2의 경우를 보면서 입력 값의 범위를 확인해야된다는 것을 다시 한 번 느낄 수 있었다. 이러한 풀이도 지금 당장은 떠오르지 않지만 실전에서는 이러한 방법이 있었다는 것을 기억해낼 수 있도록 익숙해져야 겠다고 생각했다.
