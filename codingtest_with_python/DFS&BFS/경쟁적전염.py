# condingtest_with_python_part3_DFS/BFS
# 경쟁적전염.py

# 나의 풀이 (교재 해설 참고)

# 나의 풀이 (주어진 풀이 시간 : 50분, 풀이 시간 : 1시간 12분 초 )

## s초 뒤에 x, y에 존재하는 바이러스의 종류를 출력한다. 그 위치에 바이러스 없으면 0 출력
## 주의 사항 : 인덱스는 1,1부터 시작 => 따라서 출력시 r-1, c-1 출력해야될 듯
##             1 <= k <= 1000, 0 <= s <= 10000
from copy import deepcopy

n, k = map(int, input().split())
virus_list = list(range(k + 1))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def virus(r, c, v):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and result[nr][nc] == 0:
            result[nr][nc] = v
print("---------------------------------------------------")

result = deepcopy(graph)
for second in range(1, s + 1):
    graph = deepcopy(result)
    for v in range(1, k+1):
        for r in range(n):
            for c in range(n):
                if graph[r][c] == v:
                    virus(r, c, v)
    print(f"s : {second}---------------------------------------------------")
    for i in range(n):
        for j in range(n):
            print(result[i][j], end = ' ')
        print()
print(result[x-1][y-1])
    
    
# 나의 풀이 최종 코드
from copy import deepcopy

## 시험관 크기와 바이러스 종류 정보 입력받기
n, k = map(int, input().split())

## 시험관 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

## s초 뒤에 x,y에 바이러스 종류를 출력 
s, x, y = map(int, input().split())

## 방향벡터 정의 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스 전염시키는 함수
def virus(r, c, v):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and result[nr][nc] == 0:
            result[nr][nc] = v
            
result = deepcopy(graph)
# 바이러스 증식 시작
for second in range(1, s + 1):
    # 이전 시간(초)에 증식된 정보를 고려해야 하므로 리스트 복사
    graph = deepcopy(result)
    for v in range(1, k+1):
        for r in range(n):
            for c in range(n):
                # 만약 바이러스가 존재한다면
                if graph[r][c] == v:
                    # 바이러스 증식 (상하좌우)
                    virus(r, c, v)
print(result[x-1][y-1])

# 교재 풀이
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 실험관 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 실험관 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, row, column) 삽입
            data.append((graph[i][j], 0, i, j))

## 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스부터 먼저 증식하므로)
data.sort()
q = deque(data)

## 바이러스가 퍼져나갈 수 있는 4가지 위치 설정 (방향벡터)
dr = [-1, 1, 0, 0]
dc = [0, 0,- 1, 1]

target_s, target_r, target_c = map(int, input().split())

## BFS 진행
while q:
    virus, s, r, c = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복 
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 해당 위치로 이동할 수 있는 경우:
        if 0 <= nr < n and 0 <= nc < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nr][nc] == 0:
                graph[nr][nc] = virus
                q.append((graph[nr][nc], s + 1, nr, nc))         
 
print(graph[target_r - 1][target_c - 1])

# 느낀점
"""
정말 전 문제에 비해서 너무너무 간단했지만 시간이 엄청나게 오래걸렸다.
문제 아이디어도 금방떠올라서 금방 풀 수 있을 것이라고 생각했지만
문제를 제대로 이해 못했던 부분은 다음과 같다.

1. 1초마다 하나의 바이러스만 전염되는 것으로 잘못이해 => 1초마다 모든 바이러스가 증식하되 번호가 낮은 순으로 증식

2. 2중 for문을 사용할 떄 증식한 뒤 바로 증식된 자리에 대해 또 증식이 될 수 있으므로 이전 정보를 담아두는 리스트가
    하나 더 필요했음 => 이부분을 빨리 알아차리지 못하여 뒤 늦게 deepcopy를 썼음, but,이것마저 시간 오래걸림
    
3. 또한 나는 이 문제를 완전탐색으로 풀었기 때문에 프로그래머스에서 최악의 경우의 테스트케이스를
통과하지 못했을 수도 있다, -> 따라서 교재의 BFS를 사용하는 방법을 익혀야된다.

4. BFS로 깔끔하게 풀린다. DFS와 BFS에서 방향벡터 정의하는 경우가 정말 많았고, 보통 인접노드를 처리한다는게
상하좌우 위치에 대한 정보를 처리한 다는 것이라는 것을 느꼈다.
"""
