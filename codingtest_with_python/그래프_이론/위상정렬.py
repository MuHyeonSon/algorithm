# condingtest_with_python_part2_그래프이론
# 위상정렬.py

## 위상 정렬 : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것.

# 나의 풀이(교재 참고)

from collections import deque

## 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
## 각 노드의 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
## 모든 노드에 대한 진입차수에 대한 리스트를 생성하고 전부 0으로 초기화
indegree = [0] * (v + 1)

## 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  # 진입차수 1 증가 반영
  indegree[b] += 1

## 위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌 때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for node in graph[now]:
      indegree[node] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[node] == 0:
        q.append(node)

  ## 위상 정렬을 수행한 결과 출력
  for node in result:
    print(node, end = ' ')

## 위상 정렬 실행
topology_sort()

# 교재 풀이



# 느낀점
"""
"""
