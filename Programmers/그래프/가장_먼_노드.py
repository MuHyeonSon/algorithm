# 1번 노드에서 각 다른 노드 까지의 최단 거리를 모두 구한 뒤, max값에 해당하는 노드를 모두 추출하면 될 것 같다
# 그래프 문제는 다익스트라 최단경로와, 플로이드 워셜이 있다.
# 다익스트라 => 한 지점에서 다른 지점까지의 최단 경로를 구해야하는 경우
# 플로이드 워셜 => 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우
# 이 문제는 1에서 가장 먼 노드들의 개수를 구하는 것이니까 다익스트라 최단 경로를 이용해야됨
# 그래프가 양방향이므로 graph 정보를 입력할 때, 반대로 가는 경우까지 추가 해줘야됨
import heapq

def solution(n, edge):
    answer = 0
    INF = 1e9
    
    global distance
    global graph
    
    distance = [INF for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    
    for e in edge:
        source = e[0]
        target = e[1]
        graph[source].append((target, 1)) # source에서 target으로 가는데 비용이 1
        graph[target].append((source, 1)) # 양방향이므로
    dijkstra(1)
    distance = [x for x in distance if x != INF]
    return distance.count(max(distance))

def dijkstra(start):
    global distance
    global graph
    q = []
    heapq.heappush(q, (0, start)) # (거리, 현재 노드)
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

''' 생각할 점 or 느낀점
그래프 문제이며 한 점에서 다른 점까지의 최단 경로를 구하는 문제이기 때문에 다익스트라를 사용해야된 다는 것을 알고 접근할 수 있었다.
하지만 그래프의 성질을 잠깐 놓쳤었다. 그래프가 단방향이 아닌 양방향이었기 때문에 그래프 정보를 입력할 때 a에서 b노드로 가는 정보를 입력할 때,
b에서 a로 가는 비용도 똑같이 입력했어야 했다. 다익스트라 최단경로와 플로이드 워셜 방법은 알고있다면 풀 수 있지만, 기억하지 못해내면 풀 기 어려울 수
있으므로 출제율이 낮다고 하더라도 반드시 기억해야 할 것이다.
'''
