# condingtest_with_python_part2_그래프이론
# 도시분할계획.py

# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 33분 13.54초)

## "각분리된 마을 안에 집들이 서로 연결되도록 분할해야한다", "길을 유지하는데 드는 유지비가 있다", "유지비의 합을 최소로 하고 싶다"
## -> 문제에서 저 3문장을 보고 바로 최소신장트리문제라는 것을 알 수 있었음 -> 크루스칼 알고리즘
## - 길을 없앤다 -> 그래프에서 사이클을 없앤다,

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트노드인지 확인하고, 아니라면 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 모든 노드 개수와 간선의 개수 입력 받기
N, M = map(int, input().split())
parent = [0] * (N + 1) # 부모테이블 초기회

# 모든 간선 정보 저장할 리스트 선언
edges = []

# 최종 비용을 담을 변수 선언
result = 0

# 부모테이블 상에서. 자기자신을 부모로 설정하여 초기화
for i in range(1, N + 1):
  parent[i] = i

# 모든 간선 정보 입력 받기
for _ in range(M):
  a,b,cost = map(int, input().split())
  # 튜플의 첫번째 원소를 cost로 하여 cost를 기준으로 정렬할 수 있도록 함
  edges.append((cost,a,b))

# 비용이 낮은 순서대로 모든 간선 정렬(오름차순)
edges.sort()

## 마을을 두 개로 분할하기 위해 간선하나를 없애야되는데 가장 비용이 큰 간선을 없애야 하므로 그 간선의 값을 찾기 위한 변수 선언
max_of_edge = 0

for edge in edges:
  cost, a, b = edge
  # 싸이클을 만들지 않는다면 해당 간선을 최소 신장 트리에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    # 두 원소가 속한 집합을 합침
    union_parent(parent, a, b)
    # 해당 간선을 포함함으로써 해당 간선에 대한 비용을 누적
    result += cost
    # 가장 마지막 차례에 최소 신장 트리 중 가장 큰 값이 위치하므로 그 값을 계산된 결과에서 빼기 위해
    max_of_edge = cost

# 마을을 분할하고 길을 없애고 남은 유지비 합의 최솟값을 출력
print(result - max_of_edge)

# 교재 풀이



# 느낀점
"""
다른 부분은 다 괜찮았지만, 마을을 2개로 분리하는 부분을 실제로 고려해야된다고 생각하지
못하여 그부분을 반영하지 않았다.마을을 2개로 분리하지 못했으므로 틀렸다. 어떻게 2개로 분리할 수 있을지
제대로 떠올리지 못했고, 그냥 사이클이 없는 신장트리에
간선(길)하나를 없애면 신장트리가 2개로 나눠지기 때문에 그렇게 하면 되는 거였고.
그 중에서도 간선비용(길의 유지비)이 가장 큰 것을 없애는 것이 전체 비용이 가장 최소가 되는 것이기 때문에
edges에 간선들중 최댓값을 전체 비용에서 빼주면 되는 것이었다.
빠른 시간 내에 문제를 똑바로 판단하여 아이디어를 떠올려야 된다는 것을 다시 한 번 느꼈고,
주석들에 신경쓰는 시간을 최대한 줄여야겠다고 생각했다. 

"""
