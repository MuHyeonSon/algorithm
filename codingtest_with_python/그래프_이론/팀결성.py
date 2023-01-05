# condingtest_with_python_part2_그래프이론
# 팀결성.py

# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 17분 39.10초)

## 학생 번호(0~N)
## 데이터 범위 : (1 <= N,M <= 100,000)

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트노드인지 확인하고, 루트노드가 아니라면 재귀적으로 반복해서 찾음.
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 같은 집합에 속하도록
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

N, M = map(int,input().split())
parent = [0] * (N + 1)
for i in range(N + 1):
  parent[i] = i

for _ in range(M):
  calculate_type, a, b = map(int,input().split())
  # 주어진 입력이 "팀 합치기" 연산이라면
  if calculate_type == 0:
    union_parent(parent, a, b)
  # 주어진 입력이 "같은 팀 여부 확인" 연산이라면
  else :
    # 같은 팀이라면
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    # 다른 팀이라면
    else:
      print("NO")

# 나의 풀이 (최종)

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트노드인지 확인하고, 루트노드가 아니라면 재귀적으로 반복해서 찾음.
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

N, M = map(int,input().split())
parent = [0] * (N + 1) # 부모 테이블 초기화

## 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(N + 1):
  parent[i] = i

# 각 연산을 하나씩 확인하여 처리
for _ in range(M):
  calculate_type, a, b = map(int,input().split())
  # 주어진 입력이 "팀 합치기" 연산이라면
  if calculate_type == 0:
    union_parent(parent, a, b)
  # 주어진 입력이 "같은 팀 여부 확인" 연산이라면
  elif calculate_type == 1 :
    # 같은 팀이라면
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    # 다른 팀이라면
    else:
      print("NO")


# 교재 풀이



# 느낀점
"""
그래프이론에서 학습했던, 서로소 집합 계산 알고리즘을 그대로 사용하여 어렵지 않게 풀 수 있었다.
"""
