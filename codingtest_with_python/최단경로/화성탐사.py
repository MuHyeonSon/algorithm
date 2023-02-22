# condingtest_with_python_part3_최단경로
# 화성탐사.py

# 나의 풀이 (주어진 풀이 시간 : 분, 풀이 시간 : 40분 초 )
## 가장 왼쪽 위칸인 [0][0]에서 [n-1][n-1]위치로 이동하는 최소 비용을 출력하는 프로그램 작성해라
## 한 노드에서 다른 노드로가는 최단 경로를 구하는 것 => 다익스트라 알고리즘
## 근데 이문제는 이차원임... 
## 간선이 아니라 각 칸을 지나는데 소모되는 거리는 해당 칸의 저장된 값임
## A에서 B로 가는 비용은 B
"""
import heapq
def dijkstra(start):
    # graph[i][j].append(((nr, nc), Map[nr][nc])) 
    q = []
    heapq.heappush(q, (0, start))
    distance[start[0]][start[1]] = 0
    while q:
        dist, now = heapq.heappop(q) # 우선순위 큐에서 최단거리가 가장 짧은 노드 선택
        if distance[now[0]][now[1]] < dist: # 노드가 이미 처리된 적이 있는 지 확인
            continue
        print(f'graph[now[0]][now[1]] : {graph[now[0]][now[1]]}')
        for i in graph[now[0]][now[1]]:
            cost = dist + i[1]
            if cost < distance[i[0][0]][i[0][1]]:
                distance[i[0][0]][i[0][1]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)    
for number_of_test_case in range(int(input())):
    n = int(input())
    graph = [[[] for _ in range(n)] for _ in range(n)]
    Map = []
    distance = [[INF] * (n) for _ in range(n)]
    # 맵정보 입력받기
    for _ in range(n):
        Map.append(list(map(int, input().split())))
    # 입력받은 맵정보로 distance 테이블에 값 반영
    for i in range(n):
        for j in range(n):
            distance[i][j] = Map[i][j]
    # 입력받은 맵정보로 graph 정보 입력
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < n and 0 <= nc < n and Map[nr][nc] != INF:
                    # i,j 위치와 연결된 nr, nc 노드를 저장하고 그 노드로 가기위한 비용 저장
                    #print(i, j)
                    #print(graph)
                    graph[i][j].append(((nr, nc), Map[nr][nc])) 
    #start = ((0, 0), Map[0][0])
    dijkstra(start)
    
    # 결과 출력
    for i in range(n):
        for j in range(n):
            print(distance[i][j], end = ' ')
        print()
    print(distance[n - 1][n - 1])
""" 

# 나의 풀이 (교재 해설 참고)    
import heapq
def dijkstra(start):
    r, c = start
    q = [(Map[r][c], r, c)]
    distance[r][c] = Map[r][c]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        dist, r, c = heapq.heappop(q) # 우선순위 큐에서 최단거리가 가장 짧은 노드 선택
        if distance[r][c] < dist: # 노드가 이미 처리된 적이 있는 지 확인
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 맵의 범위를 벗어나는 경우 무시
            if 0 <= nr < n and 0 <= nc < c:
                print('!!!!!!!!!!!!!!')
                cost = dist + Map[nr][nc]
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(q, (cost, r, c))
    print(distance[n - 1][n - 1])
INF = int(1e9)    
for number_of_test_case in range(int(input())):
    n = int(input())
    Map = []
    distance = [[INF] * n for _ in range(n)]
    # 맵정보 입력받기
    for _ in range(n):
        Map.append(list(map(int, input().split())))
    start = (0, 0)
    #dijkstra(start)
    
    
    r, c = start
    q = [(Map[r][c], r, c)]
    distance[r][c] = Map[r][c]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        dist, r, c = heapq.heappop(q) # 우선순위 큐에서 최단거리가 가장 짧은 노드 선택
        if distance[r][c] < dist: # 노드가 이미 처리된 적이 있는 지 확인
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 맵의 범위를 벗어나는 경우 무시
            if 0 <= nr < n and 0 <= nc < c:
                print('!!!!!!!!!!!!!!')
                cost = dist + Map[nr][nc]
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(q, (cost, r, c))
                    
    # 결과 출력
    for i in range(n):
        for j in range(n):
            print(distance[i][j], end = ' ')
        print()
    print(distance[n - 1][n - 1])
 
# 교재 풀이


# 느낀점
"""
진짜 아이디어는 풀이와 똑같이 생각했지만 아이디어를
정확히 구현해내지 못했다.... 
내가 생각하지 못한 부분은
1. 난 일반적인 다익스트라 알고리즘처럼 시작 노드에 대한 비용을 0으로 초기화했는데..

"""

"""
📰 Codingtest_with_python_part3_최단경로_화성탐사
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 최단경로 문제 풀이 느낀점
"""
