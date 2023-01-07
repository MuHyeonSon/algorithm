# condingtest_with_python_part2_최단경로
# 전보.py


# 나의 풀이 (주어진 풀이 시간 : 60분, 나의 풀이 시간 : 52분 19초)

## 도시 X에서 Y로 보내는 통로는 있지만, Y -> X 통로가 없다면 Y -> X 방향으로 메시지 못보냄
##  -> 그말은 방향이 있다는 것인 것 같음 (간선 정보), 다익스트라??
## C라는 도시에서 ***최대한 많은*** 도시로 메시지 보내고자 함.
## 시작노드(시작 도시) : C
## 구해야될 것 : 각 도시의 번호와 통로정보가 주어졌을 때,
##   1. C에서 보낸 메시지를 받게되는 도시의 총 개수 (최단거리가 INF가 아닌 도시의 개수 - 1??)
##   2. 도시들이 모두 메시지 받는데까지 걸리는 시간(가장 오래걸리는 도시의 시간?? or 모든 최단경로 비용들의 합??) 


import sys
import heapq

INF = int(1e9)

## 그래프의 노드의 개수와 간선의 개수, 시작노드를 입력받는다.
N, M, Start = map(int, sys.stdin.readline().rstrip().split())

distance = [INF] * (N + 1)
graph = [[] for i in range(N + 1)]

for _ in range(M):
    # 특정도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z
    X, Y, Z = map(int, sys.stdin.readline().rstrip().split())
    graph[X].append((Y,Z)) # X와 연결된 노드(도시)Y로 전달되는 시간은 Z

def djikstra(start):
    # 시작노드를 기준으로 우선순위 큐 구성
    q = []
    heapq.heappush(q, (0, start)) # (시간, 도시(노드))
    distance[start] = 0 # 자기자신으로 가는 비용은 0
    
    # q가 빌때까지
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리가 된 적이 있는 노드는 무시
        if distance[now] < dist:
            continue
        # 우선순위 큐에서 꺼낸 노드(가장 거리 짧은 노드)와 연결된 노드들을 처리
        for i in graph[now]:
            cost = dist + i[1]
            # 더 짧은 경로를 찾았다면 최단거리 테이블에 반영하여 갱신 및 우선순위 큐에 넣기
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

## 다익스트라 알고리즘 수행
djikstra(Start)

## C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 출력
Result_Number_Of_Cities = 0
for i in range(2, len(distance)):
    if distance[i] < INF:
        Result_Number_Of_Cities += 1
Result_Of_Time = 0
for i in range(1, len(distance)):
    if distance[i] < INF and distance[i] > Result_Of_Time:
        Result_Of_Time = distance[i]

print(Result_Number_Of_Cities, Result_Of_Time)
            

# 나의 풀이 (교재 참고하여 수정)

import heapq
import sys

INF = int(1e9)

## 그래프의 노드의 개수와 간선의 개수, 시작노드를 입력받는다.
N, M, Start = map(int, sys.stdin.readline().rstrip().split())

## 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(N + 1)]

## 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N + 1)

## 모든 간선 정보 입력받기
for _ in range(M):
    # 특정도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z
    X, Y, Z = map(int, sys.stdin.readline().rstrip().split())
    graph[X].append((Y,Z)) # X와 연결된 노드(도시)Y로 전달되는 시간은 Z


def djikstra(start):
    # 시작노드를 기준으로 우선순위 큐 구성
    q = []
    heapq.heappush(q, (0, start)) # (시간, 도시(노드))
    distance[start] = 0 # 자기자신으로 가는 비용은 0
    
    # q가 빌때까지
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리가 된 적이 있는 노드는 무시
        if distance[now] < dist:
            continue
        # 우선순위 큐에서 꺼낸 노드(가장 거리 짧은 노드)와 연결된 노드들을 처리
        for i in graph[now]:
            cost = dist + i[1]
            # 더 짧은 경로를 찾았다면 최단거리 테이블에 반영하여 갱신 및 우선순위 큐에 넣기
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

## 다익스트라 알고리즘 수행
djikstra(Start)

## C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 출력
Result_Number_Of_Cities = 0 # 도달할 수 있는 노드의 개수
Result_Of_Time = 0 # 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리

for d in distance:
    # 도달할 수 있는 노드의 경우
    if d != INF:
        Result_Number_Of_Cities += 1
        Result_Of_Time = max(Result_Of_Time, d)

## 시작 노드는 제외해야 하므로 Result_Number_Of_Cities - 1
print(Result_Number_Of_Cities - 1, Result_Of_Time)

# 교재 풀이




# 느낀점
"""
막혔던 점
1. 빠른 입력을 받기 위한 sys.stdin.readline()이 문제를 에러를 발생시켰고,
해결 방법을 잘 알지 못하여서 여러 방법을 시도해봄
    -> rstrip()을 하였더니 정상적으로 실행됐음
2. 다익스트라 알고리즘 구현하다가 우선순위큐에 더짧은 경로를 발견한 노드를 넣는 부분에
대해서 튜플의 거리정보를 넣는 것을 빠뜨려 에러 발생시킴
    -> 계속해서 원인을 찾아보고 해결하고자 했고, print로 변수들 찍어보면서
    원인을 파악하고자 했음. but, 실제 코테 환경에서 출력 값 찍어볼 수 있는지 모르니까
    이러한 방법이 없었다면 무조건 에러해결못하고 틀렸을 것 같다..

풀면서 느낀점
1. 문제를 읽고 다익스트라 문제 라는 것이 맞는지 확실하게 알기 어려운 부분이라고
생각한 건 최대한 빠른 경로나, 시간을 찾는 다는 말이 없었고, 대신에 "위급상황"이라는 말이
있었다. 그래서 실전에서 마주하였다면 빠르게 떠올리는 것이 힘들었을 지도 모른다.
2. 정리해보니, 일방향적인 통로라고 했으니 양방향을 고려할 필요가 없는 점과. 
도시 C에서 출발한 다는 점이 플로이드 워셜알고리즘을 사용할 필요가 없다고 생각했다.\
    
 해설을 읽고나서,
 N과 M범위가 충분히 크다고 하였는데 (1 <= N <= 30,000), (1<=M<=200,000)으로
 나는 데이터 범위를 전혀 고려하지 않은채 풀었다는 것을 느꼈고, 
 100만개 이상의 데이터가 들어갈 수 있는 크기의 리스트를 선언하는 경우는 적은데
 이번 문제는 간선의 개수만 최대 20만개였으므로 충분히 데이터 범위가 큰 문제라는
 것을 느꼈다.

"""
