# condingtest_with_python_part3_DFS/BFS
# 인구이동.py

# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 분 초 )
## 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면, 두 나라가 국경선을 오늘 하루동안 연다.
## 위에 조건에 따라 열어야하는 국경선 모두 염 (국경선 연 나라들 목록 만들?)
## 
from collections import deque
#from copy import deepcopy

n, L, R = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

count = 0



def bfs(start):
    global count, n, L, R
    q = deque([start])
    union = []
    r, c = start
    union.append((r, c, graph[r][c]))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 벗어나지 않는다면
            if 0 <= nr < n and 0 <= nc < n:
                # 국경선 여는 조건 만족하면
                if L <= abs(graph[nr][nc] - graph[r][c]) <= R:
                    # 인구 이동 시작
                    count += 1
                    q.append((nr, nc))
                    union.append((nr, nc, graph[nr][nc]))
                    sum_population = 0
                    for i in range(len(union)):
                        sum_population += union[i][2]   
                    union_population = int(sum_population / len(union))
                    
                    for nation in union:
                        a, b, c = nation
                        graph[a][b] = union_population
 
#temp = deepcopy(graph)
for i in range(n):
    for j in range(n):
        bfs((i, j))
        #graph = deepcopy(temp)

print(count)                 


# 교재 풀이
from collections import deque

## 땅의 크기(N), L, R값을 입력받기
N, L, R = map(int, input().split())

## 전체 나라의 정보(N x N)를 입력받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0

## 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(r, c, index):
    # (r, c)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((r, c))
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((r, c))
    union[r][c] = index # 현재 연합의 번호 할당
    summary = graph[r][c] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 떄까지 반복(BFS)
    while q:
        r, c = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nr < N and 0 <= nc < N and union[nr][nc] == -1:
                if L <= abs(graph[r][c] - graph[nr][nc]) <= R:
                    q.append((nr, nc))
                    # 연합에 추가
                    union[nr][nc] = index
                    summary += graph[nr][nc]
                    count += 1
                    united.append((nr, nc))
    
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

## 더이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == N * N:
        break
    total_count += 1

## 인구 이동 횟수 출력
print(total_count)    
    

# 느낀점
"""
BFS 사용 및 연합을 시키는 아이디어는 맞게 구현하였으나 인구이동수를 구하는 것에 문제가 있었다.
교재에서는 나와 다르게 union이라는 2차원리스트를 사용하였고, graph의 모든 위치에서 모든 나라가 연합 처리가 될 수 있을 때까지 반복하였다. 즉 NxN의 모든 위치를 찍었고,
그렇게 다 찍는 동안 count의 개수를 하나씩 증가 시켰다. 솔직히 이해가 잘 안간다.

1. 아이디어를 잘 떠올렸다고 생각했지만, 인구 이동 수를 구하는 것에서 문제가 발생했다.
내가 작성한 것은 1일차만 인구이동을 수행하도록 코드를 작성했지만 인구이동이 더이상 불가할 때까지 계속해서
반복을 했어야한다.

2. 또한 해설에서는 이미 방문을 했는지, union이라는 그래프를 하나 더 만들어서 해당 나라를 방문 했는지 여부를 기록하였는데
난 이 과정도 뺴먹었다.인구이동을 반복 할 수 없을 떄까지 bfs를 반복한다는 것, 방문 정보를 union이라는 2차원리스트를 통해 표기한다는 점 둘 다
생각해내지 못했다.. 방문정보 표기는 단순히 union에 포함되었냐 아니냐로 구분할 수 있다고 생각하였다.

3. 함수 밖에서 선언한 변수가 원래 함수 안에서 그 값을 불러오는 것은 가능하지만 값읗 수정해도 변경된 값이 함수 밖에서 변경이 되지 않는다는 것을
    이번에 제대로 짚고 넘어갈 수 있었다.

"""
