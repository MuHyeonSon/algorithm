# condingtest_with_python_part2_그래프이론
# 서로소집합을_활용한_사이클판별.py

# 나의 풀이

# 나의 풀이 (최종)

# 교재 풀이
## 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

## 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a) # a의 루트노드를 찾아서 변수에 저장
  b = find_parent(parent, b) # b의 루트노드를 찾아서 변수에 저장
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(union 연산)의 수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모테이블 상에서, 부모를 자기자신으로 초기화
for i in range(1, v + 1):
  parent[i] = i

cycle = False # 사이클 발생여부
for _ in range(e):
  a, b = map(int, input().split())
  # 사이클이 발생한 경우 종료
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)


if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")
    

# 느낀점
"""
"""
