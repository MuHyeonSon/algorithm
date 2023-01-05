# condingtest_with_python_part2_그래프이론
# 크루스칼알고리즘.py

# 나의 풀이(교재 참고)

## 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지, 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

## 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else :
    parent[a] = b

## 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

## 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

## 부모테이블 상에서, 자기자신을 부모로 설정
for i in range(1, v + 1):
  parent[i] = i

## 모든 간선에 대한 정보 입력받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
  edges.append((cost, a, b))

## # 간선을 비용순으로 (오름차순) 정렬
edges.sort()

## 간선을 하나씩 확인하며 처리
for edge in edges:
  cost, a, b = edge  
  # 싸이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)



# 교재 풀이



# 느낀점
"""
"""
