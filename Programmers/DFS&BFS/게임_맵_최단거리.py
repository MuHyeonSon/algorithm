# 미로찾기나 상하좌우맵에서 최소이동거리 => BFS이용해서 이전 위치에 1씩 더하기
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 방향벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = deque([(0,0)])
    while queue:
        pos = queue.popleft()
        r = pos[0]
        c = pos[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                maps[nr][nc] += maps[r][c]
                queue.append((nr, nc))
    answer = maps[n-1][m-1]
    if answer == 1:
        return -1
    return answer
