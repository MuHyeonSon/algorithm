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

# 교재 풀이

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

# 교재 풀이가 훨씬 간결하다는 것을 느꼈고 m을 하나씩 빼는 방식으로
#count하는 것이 변수를 하나 더 생성하는 것보다 훨씬 효율적이라는 생각을 했다.
