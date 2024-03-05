# dfs
def dfs(graph, v, visit):
    visit[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if not visit[node]:
            dfs(graph, node, visit)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * len(graph)
start = 1
dfs(graph, start, visit)

# bfs
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')
    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if not visited[v]:
                queue.append(v)
                print(v, end=' ')
                visited[v] = True
            
        

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)

# 느낀점
"""
사용안하면 까먹으니 계속 보자
"""
