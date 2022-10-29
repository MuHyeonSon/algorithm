# condingtest_with_python_part2_greedy
# greedy_숫자카드게임.py

# 나의 풀이

# N : 행의 개수, M : 열의 개수
N, M = map(int,input().split())
#card = [[0]*M for _ in range(N)]
card = []
for _ in range(N):
  card.append(list(map(int,input().split())))
# 선택한 행의 그 다음 행에서 가장 작은 수를 뽑아야한다
# 이게 가장 큰 수가 되어야함
# 그리디는 당장 최선의 선택을 한다고 했음

maximum = min(card[0]) # 규칙에 따라 선택했을 대 가장 작은 수를 저장할 변수
# 결국 모든 행에 대해 각 행에서 가장 작은 숫자들 중 가장 큰 값을 뽑아야 됨!

for i in range(N):
  if maximum < min(card[i]):
    maximum = min(card[i])

# 최종 결과 출력
print(maximum)
  
# 문제 해설
# -> 이 문제를 푸는 아이디어 : 각 행마다 가장 작은 수를 찾은 뒤, 그 수 중에서 가장 큰 수를 찾는 것.


# 교재풀이 1

n, m = map(int,input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int,input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = min(data)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력


# 교재풀이 2 (2중 반복문)

n, m = map(int,input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int,input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value,a)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result,min_value)

print(result) # 최종 답안 출력

# 내가 짠 코드와 교재풀이 1을 비교했을 때 굳이 2차원리스트를 만들지 않아도 된다는
# 것을 알게 되었다. 아직은 효율적인 코드보다 문제 자체를 그대로 코드에 구현하는 것이
# 더 익숙한 것 같다. 또한 result 변수도 결국 max값을 저장할 것이기 때문에 0으로
# 초기화 했어도 문제가 되지 않았다. (범위를 확인해봐도 1~10000 이하였으니)
