# condingtest_with_python_part2_최단경로
# 미래도시.py

# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : )
## x번 회사 : 물건 판매할 곳
## K번 회사 : 소개팅상대가 있는 회사
## N : 회사 개수
## K번 회사 갔다가 x번 회사로 갈거임 (1 -> k -> x)

## 문제를 읽고서 든 생각
## 최단경로를 구하는 건 파악했음 but, 다익스트라를 쓸지 최단 경로를 쓸지 정해야되는데
## 이동하고자 하는 곳이 특정 지점에서 다른 지점까지 하나의 경로만 구하는게 아니라
## 2곳을 방문하는 것에 있어 최단 경로를 구해야되기 때문
## 시작지점에서 k까지의 최단거리와 k에서 x까지의 최단거리를 구하는 것인 것 같은데 그러면
## 모든지점에서 다른 모든지점의 최단 거리를 구하는 플로이드워셜 알고리즘으로 구현하는 것이 맞지 않을까?
## 만약 다익스트라 라면 알고리즘을 두 번 수행(1->k, k->x) 해야 찾을 수 있는 것 아닐까??
## 일단 다익스트라로 구현-> 안 돼
## 걍 플로이드 워셜로 ㄱ
"""
import sys
import heapq

## 전체 회사의 개수(노드의 개수) 경로 개수(간선 개수) 입력 받기
N, M  = map(int, sys.stdin.readline().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for i in range(N + 1)] ######### 2차원 리스트 DP 테이블

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split()) # a에서 b로 가는 비용이 c
    #print(f'a : {a}, b : {b}')
    graph[a][b] = 1 # 특정 회사가 다른 회사와 연결되어 있다면 1만큼의 시간이 걸림
    
X, K = map(int, sys.stdin.readline().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1): 
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
K_time = graph[1][K]
X_time = graph[K][X]
print(f'k_time : {K_time}')
print(f'x_time : {X_time}')
result = 0

if K_time == INF or X_time == INF:
    result == -1
else:
    result = K_time + X_time

print(result)
"""


# 나의 풀이 (교재 해설 참고)

## 전체 회사의 개수(노드의 개수) 경로 개수(간선 개수) 입력 받기
import sys

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

## 노드의 개수 및 간선 개수를 입력받기
N, M  = map(int, sys.stdin.readline().split()) # 교재에서는 sys.stdin.readline()안씀
## 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for i in range(N + 1)] ######### 2차원 리스트 DP 테이블

## 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

## 각 간선에 대한 정보 입력받아, 그 값으로 초기화
for _ in range(M):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, sys.stdin.readline().split()) # a에서 b로 가는 비용이 c
    graph[a][b] = 1 # 특정 회사가 다른 회사와 연결되어 있다면 1만큼의 시간이 걸림
    graph[b][a] = 1 ################################# 내가 놓친 부분 "양방향으로 이동할 수 있다는 점을 고려하지 못함"

## 거처 갈 노드 최종 목적지 노드 입력받기    
X, K = map(int, sys.stdin.readline().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1): 
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][K] + graph[K][X]

# 도달할 수 없는 경우, -1을 출력
if result >= INF:
    print("-1")
# 도달할 수 있는 경우, 최단 거리를 출력
else :
    print(result)


# 교재 풀이


# 느낀점
"""
다 구해놓고 2차원리스트 초기화할 줄 몰라서 이렇게 문제가 생긴 것이 너무 분했다..
진짜 이 기본적인걸 몰라갖고..
그리고 "="을 실수로 "=="으로 써갖고 원인 찾는데 몇 십분을 소비했다는 게 용납이 안 된다.
장난하는 것도 아니고, 이걸 왜 못찾고 있어서 실전에서 이런 말도 안되는 실수하면 어떡하겠냐고 생각했지만
어찌됐던 이번 문제도 마찬가지로 쉽게 해결될거라 생각했지만 많이 부족하다는 것을 느꼈고
내가 막혔던 부분을 정리해보자면 다음과 같다.

1. 2차원 리스트 생성 및 초기화
2. 플로이드워셜 알고리즘 구현 제대로 못함(graph와 distance 둘 다 생성하지않고(그래프 정보필요x), DP테이블만 채우면 됐음)
3. "="을 "=="으로 실수한 것을 몇 십분동안 못찾은 것.
4. 문제에서 양방향으로 이동가능하다고 말하였으나 이 알고리즘과 그래프에 대한 지식이 부족하여
    해당 부분을 고려하지 않았음..
    
또한 해설을 보며 알게된점은 다음과 같다.
1. 해당 문제가 전형적인 플로이드 워셜 알고리즘 문제라는 것.
2. 범위가 한정적이기 때문에(1 <= N, M, K <= 100) 플로이드 워셜 알고리즘을 이용해도 빠르게 풀 수 있어
구현이 간단한 플로이드 워셜 알고리즘 이용하는 것이 유리하는 것.

그래도 해설을 보며 이 문제의 핵심 아이디어인 "1번노드 K까지의 최단거리 + K에서 X까지 최단거리"
잘 떠올렸고, 플로이드 워셜 알고리즘을 사용하는 것이 맞다는 판단을 잘했다는 점에서
내 자신을 칭찬해줘야 된다고 생각하고 계속해서 연습해나가면서 실수를 줄이자고 생각하였다.
"""



# 교재 풀이




# 느낀점
"""
다 구해놓고 2차원리스트 초기화할 줄 몰라서 이렇게 문제가 생긴 것이 너무 분했다..
진짜 이 기본적인걸 몰라갖고 무슨 코테를 본다고
"""
