# 미로탈출
## 미로 탈출 문제는 => BFS로 먼저 접근해보자
#괴물 => 0
#괴물 없는 부분 => 1
# 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수
# 시작칸과 마지막칸을 모두 포함해서 계산 (마지막칸은 항상 1이며 n,m의 존재)
# 너비우선탐색을 할경우 인접한 노드를 우선적으로 방문하는건데 최소칸의 개수를 어떻게 구할까 n,m 까지 가게해야되는데
# 이동위치 전에서 현재 이동위치에 1을 더하여 기록해 놓으면 됨
# 0에는 가지말고, 1이면 이동하되 이전 위치에서 1을 더하면 됨, 1이면 visit이 False 1이상이면 True로 기록하면 된다. 0이면 아예 이동자체를 안하고
# bfs는 큐 자료구조 이용하고 collections 에서 deque 임포트해서 사용함, 삽입은 pop.left로, while문 사용
# miro 맵을 하나는 기록용 하나는 참조용으로 두개를 두어도 괜찮을듯

from collections import deque
from copy import deepcopy

n, m = map(int, input().split()) # n : 행, m : 열
miro = []
for _ in range(n):
    row = list(input())
    row = [int(s) for s in row]
    miro.append(row)
    
original_miro = deepcopy(miro)

# 상하좌우 방향벡터    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(miro, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        #miro[r][c] = miro[node[0]][node[1]] # 방문 처리
        r, c = node[0], node[1]
        #miro[r][c] += 1 # 방문 처리 (단순히 1더하는게 아니라 이전 위치에 1을 더해야된다고)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < n) and (0 <= nc < m) and (miro[nr][nc] == 1):
                queue.append((nr, nc))
                miro[nr][nc] += miro[r][c]
    
bfs(miro, (0,0))
for i in range(n):
    print(miro[i])
print(miro[n-1][m-1])

# 생각해볼점
"""
다 구현해놓고 이코테에서 알려준 기본 bfs만 생각하다가 계속 헤맸다. 이전 위치에 1을 더하는 것이 곧 방문처리이고 
방문처리는 큐에서 데이터를 꺼낸 뒤 이루어지는 것이라고 생각했다. 그래서 다른 인접노드를 찾는 과정에서는 방문처리를 하면 안된다고 생각했기 때문에
계속해서 헤맸던 것이다.

결론 : bfs 동작원리는 기억하되, 어떻게든 기본 bfs의 동작과정을 모두 따르려 하지 말자
"""
