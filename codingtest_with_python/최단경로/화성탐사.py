# condingtest_with_python_part3_최단경로
# 화성탐사.py

# 나의 풀이 (주어진 풀이 시간 : 분, 풀이 시간 : 40분 초 )
## 가장 왼쪽 위칸인 [0][0]에서 [n-1][n-1]위치로 이동하는 최소 비용을 출력하는 프로그램 작성해라
## 한 노드에서 다른 노드로가는 최단 경로를 구하는 것 => 다익스트라 알고리즘
## 근데 이문제는 이차원임... 
## 간선이 아니라 각 칸을 지나는데 소모되는 거리는 해당 칸의 저장된 값임
## A에서 B로 가는 비용은 B

# 나의 풀이 (교재 해설 참고)
import heapq
def dijkstra(start):
    # graph[i][j].append(((nr, nc), Map[nr][nc])) 
    q = []
    heapq.heappush(q, (0, start))
    distance[start[0]][start[1]] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in graph[now[0]][now[1]]:
            cost = dist + i[1]
            if cost < distance[i[0][0]][i[0][1]]:
                distance[i[0][0]][i[0][1]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)    
for number_of_test_case in range(int(input())):
    n = int(input())
    start = (0, 0)
    graph = [[] * (n + 1) for _ in range(n + 1)]
    Map = []
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    # 맵정보 입력받기
    for _ in range(n):
        Map.append(list(map(int, input().split())))
    # 입력받은 맵정보로 distance 테이블에 값 반영
    for i in range(n):
        for j in range(n):
            graph[i][j] = Map[i][j]
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
                    graph[i][j].append(((nr, nc), Map[nr][nc])) 

    dijkstra(start)
    
    # 결과 출력
    print(distance[n - 1][n - 1])
    

# 교재 풀이


# 느낀점
"""
"""

"""
📰 Codingtest_with_python_part3_최단경로_화성탐사
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 최단경로 문제 풀이 느낀점
"""
