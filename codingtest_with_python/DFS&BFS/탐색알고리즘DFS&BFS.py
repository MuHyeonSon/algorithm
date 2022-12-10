# condingtest_with_python_part2_DFS/BFS
# 탐색알고리즘DFS&BFS.py

## DFS(Depth-First-Search) 깊이 우선 탐색 : 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘 
## 인접 행렬 방식은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식 (2차원 리스트로 구현)
## 인접 리스트 방식은 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결 (2차원 리스트로 구현)

## 5-6.py 인접 행렬 방식 예제

INF = 999999999

### 2차원 리스트를 이용해서 인접 행렬 표현

graph = [
    [0,7,5]
    [7,0,INF]
    [5,INF,0]
]

print(graph)

## 5-7.py 인접 리스트 방식 예제

graph = [[] for _ in range(3)]

### 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)

## DFS는 스택 자료구조를 이용함 (탐색 수행함에 있어 O(N)소요)
## 동작방식
### 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
### 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리함, 
###    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
### 3. 과정 2를 수행할 수 없을 때까지 반복

## 5-8.py DFS 예제

### DFS 함수 정의

def dfs(graph,v,visited):
  # 방문 처리
  visited[v] = True
  print(v, end = ' ')
  
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트로 표현
visited = [False]*9

dfs(graph, 1, visited)
