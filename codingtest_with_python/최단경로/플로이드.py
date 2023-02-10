# condingtest_with_python_part3_최단경로
# 플로이드.py

# 나의 풀이 (교재 해설 참고)
INF = 1e9

v = int(input()) # 도시의 개수
e = int(input()) # 버스의 개수

graph = [[INF] * (v + 1) for _ in range(v + 1)]

## graph 초기 세팅(자기자신으로 가는 것들은 모두 0으로 초기화)
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            graph[i][j] = 0

## 간선정보 (버스비용 정보 입력받기)
for _ in range(e):
    # a에서 b로 가는 비용이 c
    if c < graph[a][b]:
        a, b, c = map(int, input().split()) 
        graph[a][b] = c
 
## 플로이드 워셜 알고리즘 수행 
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])   

## 결과 출력
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()


# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 분 초 )

## 모든 도시의 쌍 a,b 에 대해 a에서 b로 가는 데 필요한 최소비용을 구하는 것
## 모든 노드에서 다른 모든 노드로 가는 최단거리 구하기 => 플로이드 워셜 알고리즘 사용
## 도시 => 노드
## 버스 => 간선
## 위와 같이 생각하고 풀어보자
INF = 1e9

v = int(input()) # 도시의 개수
e = int(input()) # 버스의 개수

graph = [[INF] * (v + 1) for _ in range(v + 1)]

## graph 초기 세팅(자기자신으로 가는 것들은 모두 0으로 초기화)
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            graph[i][j] = 0

## 간선정보 (버스비용 정보 입력받기)
for _ in range(e):
    # a에서 b로 가는 비용이 c
    a, b, c = map(int, input().split()) 
    graph[a][b] = c
 
## 플로이드 워셜 알고리즘 수행 
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])   

## 결과 출력
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if graph[i][j] == INF:
            print(0, end = ' ')
        else:
            print(graph[i][j], end = ' ')
    print()

# 교재 풀이

# 느낀점
"""
당연하게 플로이드 워셜알고리즘을 써야된다고 생각하였는데
예시와 다르게 결과가 나와 무엇이 문제인지 계속 생각해봤지만 찾지 못하였다.
다시 문제를 잘 살펴보니 시작도시와 도착도시를 연결하는 노선이 하나가
아닐 수 있다는 것을 보고 입력예시를 잘 살펴봐야헸다. 일반적인
플로이드워셜알고리즘과 다르게 a,b가 중복되는 것이 있었다. 즉 간선이 여러개가
존재하는 문제였다. 최솟값을 구하는 것이므로 이 중복되는 간선 중에서 당연히,
가장 짧은 간선을 택하는 방식으로 플로이드워셜알고리즘 코드를 수정해야 문제를 
해결할 수 있었던 것이다.
이러한 쉬운 문제를 해결하지 못했다는 것에 대해 반성해야겠다고 생각하였고,
반드시 기억해놓았다가 다음에 비슷한 문제를 마주치면 이문제를 꼭 떠올릴 것이다.
"""
