# condingtest_with_python_part3_DFS/BFS
# 연구소.py

# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간  60분 초 )
import copy
from collections import deque
import time

n, m = map(int, input().split())
Map = []

for _ in range(m):
    Map.append(list(map(int, input().split())))
## bfs로 모두 탐색하다가 2를 발견하면 인접노드(상하좌우)가 1인 곳을 찾는다.
## 2의 상하좌우인 곳 중 그 위치의 원소 값이 0인 곳은 모두 2로 갱신
## 새로 벽을 세울 위치를 3중 반복문 돌려서 모든 경우 다 탐색 해봐?
## 2의 인접노드를 볼거니까 BFS이용?
start_time = time.time()

max_value = 0

zero_list = []

temp_Map = copy.deepcopy(Map)

def bfs(temp_Map, start):
    #q = deque([start])
    a, b = start # 2 인 곳(바이러스가 있는 곳)
    # temp_Map[a][b] = -1 # 방문 표시
    # 상하좌우 이동방향 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr = a + dr[i]
        nc = b + dc[i]
        if 0 <= nr < n and 0 <= nc < m and temp_Map[nr][nc] != 1:
            temp_Map[nr][nc] = 2
        
    

 
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0:
            zero_list.append((i, j)) # 빈칸인 a행 b열을 빈칸 리스트에 추가

for i in range(len(zero_list)):
    for j in range(len(zero_list)):
        for k in range(len(zero_list)):
            if i == j or i == k or j == k:
                continue
            if temp_Map[zero_list[i][0]][zero_list[i][1]] != 0 or temp_Map[zero_list[j][0]][zero_list[j][1]] != 0 or temp_Map[zero_list[k][0]][zero_list[k][1]] != 0:
                continue
            else:
                temp_Map[zero_list[i][0]][zero_list[i][1]] = 1
                temp_Map[zero_list[j][0]][zero_list[j][1]] = 1
                temp_Map[zero_list[k][0]][zero_list[k][1]] = 1
                for row in range(n):
                    for column in range(m):
                        if temp_Map[row][column] == 2:
                            bfs(temp_Map, (row, column))
                count = 0
                for r in range(n):
                    for c in range(m):
                        if temp_Map[r][c] == 0:
                            count += 1
                max_value = max(max_value, count)
                temp_Map = copy.deepcopy(Map)

print(max_value)
                        
end_time = time.time()

print(f'수행시간 : {end_time - start_time}')            
                
                
# 교재 풀이
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

## 4가지 이동 방향에 대한 리스트
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = 0

## 깊이 우선 탐색(DFS)를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if 0 <= nr < n and 0 <= nc < m:
            if temp[nr][nc] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nr][nc] = 2
                virus(nr, nc) 
    
## 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

## 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기를 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result) 


# 느낀점
"""
문제는 풀었지만 어떻게든 구현했지만 dfs bfs를 거의 활용하지 않고
완전탐색과 가깝게 풀었더니 실행시간이 4초가 넘게 나왔다.

해설을 확인해보니 벽을 3개를 설치하는 모든 경우의 수를 다 계산해야 된다고 하였고
나또한 그렇게 구현하였다.

벽을 설치하는 모든 경우의 수는 최악의 경우일때이니 8x8 크기일 때 64 C 3 이다.
이것이 100,000보다 작은 수 이기 때문에 모든 경우의 수를 다 고려해도 제한 시간 안에
문제를 해결할 수 있다고 한다.

그리고 모든 조합을 계산할 때 파이썬의 combinations? 조합 라이브러리 이용하거나 DFS/BFS를 적절히
사용할 수 있다고 하는데 나는 이부분에 있어서 실수를 했거나 효율적으로 코드를 작성하지 못한 것이다.

내가 효율적으로 작성하지 못한 부분에 대한 교재의 풀이는 다음과 같다.
    1. BFS가 아닌 DFS를 이용하였다.
    2. DFS를 두 개를 구현해 각각 기능을 달리 하였다.
        (1) 각각 바이러스가 사방으로 퍼지도록 하는 DFS 함수
            => 나는 그냥 단순히 DFS를 이용하지 않고, 맵전체를 확인하며 2인 위치에 대해 상하좌우를 2로 만들었다.
                DFS를 이용한다면 하나씩 for문 돌리면서 채우지 않고 재귀적으로 퍼뜨릴 수 있었다.
        (2) 울타리를 설치하고, 매번 안전 영역의 크기를 계산하는 DFS 함수
            => 나는 세 개의 울타리를 설치하는 것을 시간이 오래 걸리게 3중 for문으로 구현했다..
        
솔직히 재귀함수로 해설이 되어있어 코드가 잘 이해가 되지 않는다.
이 풀이를 그대로 외우는 것이 좋을지 이 풀이를 참고하여 내 방식대로 코드를 구현하여
익히는 것이 좋을 지 솔직히 잘 모르겠다.. 우선은 시간복잡도 및 효율성등을 고려하여 교재코드만을 보고 이해하고 익히는 방향으로
하는 것이 좋지 않을 까 생각했다.

"""
