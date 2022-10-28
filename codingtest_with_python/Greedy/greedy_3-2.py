# 큰 수의 법칙 greedy_3-2.py

#나의 풀이

# ek다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여
# 가장 큰 수를 만드는 법칙

# N 배열의 크기
# M 숫자가 더해지는 횟수
# K 특정 인덱스의 수가 연속해서 k번까지만 더해질 수 있음

N, M, K = map(int, input().split())
l = list(map(int, input().split()))
total_sum = 0
count = 0

l.sort(reverse=True)

while count < M:
  for i in range(K):
    if count == M:
      break
    total_sum += l[0]
    count += 1
  if count < M:
    total_sum += l[1]
    count += 1
    

print(total_sum)

# 교재 풀이 (단순하게 푸는 예시답안)

# n,m,k를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩 빼기
  if m == 0 # m이 0이라면 반복문 탈출
    break
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 뺴기

print(result) # 최종 답안 출력

# 예시 답안

# n,m,k를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산 ( int(M / (K+1) * k + M % (k + 1) )
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력


# 교재 풀이가 훨씬 간결하다는 것을 느꼈고 m을 하나씩 빼는 방식으로
#count하는 것이 변수를 하나 더 생성하는 것보다 훨씬 효율적이라는 생각을 했다.

# 추가로 M이 100억 이상처럼 커져 시간초과 판정을 받을 수 있는 것을 고려했을 때
# 반복문을 이용하지 않고 수학적 아이디어로 간단하게 풀 수 있다는 것을 알게 되었다.
# 따라서 M의 범위도 잘 확인해봐야된다는 것을 생각해보는 계기가 되었다.
# 보통의 경우 반복문을 이용하는 것을 먼저 떠올리기 때문이다.

