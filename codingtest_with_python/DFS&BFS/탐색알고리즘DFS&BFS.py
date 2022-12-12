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


## BFS는 큐 자료구조 이용하는 것이 정석 (탐색 수행함에 있어 O(N)소요)
## 동작방식
### 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
### 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 하고 방문 처리함.
### 3. 과정 2를 수행할 수 없을 때까지 반복

## 5-9.py BFS 예제

from collections import deque

def bfs(graph,visited):
  queue = deque()
  queue.append(graph[1][0]) # 시작 노드를 큐에 삽입
  visited[1] = True # 시작 노드 방문 처리
  while visited[1:] not in False:
    node = queue.popleft()
    for n in graph(node):
      if visited[n] == False:
        queue.append(graph[n])
        visited[node] == True 



### BFS 함수 정의

from collections import deque

#### 내가 구현한 것
def bfs(graph,start,visited):
  queue = deque()
  queue.append(start) # 시작 노드를 큐에 삽입
  visited[v] = True # 시작 노드 방문 처리
  while False in visited[1:] or len(queue) != 0: ##########################
    node = queue.popleft()
    print(node, end = ' ')
    for adjacency_node in graph[node]:
      if visited[adjacency_node] == False: ##########################
        queue.append(adjacency_node)
        visited[adjacency_node] = True 

#### 교재에서 구현한 것
def bfs(graph,start,visited):
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue: ##########################
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]: 
      if not visited[i]:##########################
        queue.append(i)
        visited[i] = True

#### 각 노드가 연결된 정보를 리스트 자료형으로 표현
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

#### 각 노드가 방문된 정보
visited = [False] * 9

bfs(graph,1,visited)
