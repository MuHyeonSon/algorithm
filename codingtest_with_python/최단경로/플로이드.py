# condingtest_with_python_part3_최단경로
# 플로이드.py

# 나의 풀이 (교재 해설 참고)


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
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c
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

"""

"""
📰 Codingtest_with_python_part3_최단경로_플로이드
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 최단경로 문제 풀이 느낀점
"""
