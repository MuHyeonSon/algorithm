# condingtest_with_python_part3_DFS/BFS
# 특정거리의도시찾기.py

# 나의 풀이 (교재 해설 참고)
from collections import deque

n, m, k, x = map(int, input().split())

## X에서 부터 각 노드까지에 대한 최단 거리를 저장할 리스트 선언 및 초기화
distance = [-1] * (n + 1)

q = deque([x])
distance[x] =  0 # 출발도시에서 출발도시로 가는 거리는 0

## 도로(간선)정보 입력 받기
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

if k not in distance:
    print(-1)
else:
    distance.sort()
    for i in range(1, len(distance)):
        if distance[i] == k:
            print(i)
            
## 교재 풀이의 출력 방식
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)


# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 못 품 )
## 특정 도시 X로부터 최단거리가 정확히 K인 모든 도시의 번호를 출력
## K == 1이라면 인접노드들을 출력 (단방향*****)
"""
from collections import deque

def bfs(graph, start, visited, k):
    q = deque([start])
    visited[start] = True
    distance = [0] * len(graph)
    result_list = []
    count = 0
    while q:
        v = q.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] == True
                if count == k:
                    result_list.append(i)
    return result_list
                    

## 도시의 개수 n, 도로의 개수 m, 거리정보 k, 출발 도시 번호 x 입력 받기
n, m, k, x = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

l = bfs(graph, x, visited, k)
l.sort()
for e in l:
    print(e)

"""


# 느낀점
"""
문제를 처음보고 다익스트라 최단거리 알고리즘 문제라는 생각이 들었지만
굳이 최단거리알고리즘을 구현하지 않아도 풀 수 있지 않을까 하는 생각이들었다.
왜냐하면 간선의 비용이 모두 같기 떄문이다..

내가 떠올리지 못했던 구현은 다음과 같다.
1. X로부터 각 노드에 대한 거리를 계산하는 것.
=> distance[현재 queue에서 꺼낸 노드의 인접노드] = distance[현재queue에서 꺼낸 노드] + 거리
    이것은 최단경로 알고리즘인 다익스트라 알고리즘에 구현부분 중 하나로 이것만
    떠올렸다면 문제를 풀 수 있었을 것이다. 하지만 이것을 떠올리지 못하고 이상한 방식으로
    그냥 q에서 꺼낼때마다 x에 대한 거리가 1씩늘어난다고 가정하고 코드를 짠 것이다.
2. visited를 꼭 필수적으로 구현해도 되지 않는다는 것.
=> 해설에서는 distance 리스트 하나만을 사용해 방문하지 않은 노드는 -1이라는 값을 설정하여
    방문 여부를 표현하였다. 이러한 방식도 잘 기억해둘 것이다.
"""

"""
"""
