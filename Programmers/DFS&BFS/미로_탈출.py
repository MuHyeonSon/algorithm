# 미로탈출 => bfs로 먼저 접근해보자
# 레버를 당긴 뒤에 출구로 이동할 수 있음
# 한 칸 이동에 1초 걸림
# 탈출할 수 없다 => 시간맵의 0이다 => return -1
from collections import deque

def solution(maps):
    answer = 0
    num_row = len(maps)
    num_column = len(maps[0])
    # 시작지점 S, 출구 E, 레버 L 위치 찾기
    for i in range(num_row):
        for j in range(num_column):
            if maps[i][j] == 'S':
                S = (i,j)
            elif maps[i][j] == 'E':
                E = (i,j)
            elif maps[i][j] == 'L':
                L = (i,j)
                
    time_map = [[0 for _ in range(num_column)] for _ in range(num_row)]
    
    # 방향벡터(상하좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = []
    for finish in S, L:
        queue = deque([finish])
        time_map = [[0 for _ in range(num_column)] for _ in range(num_row)]
        while queue:
            r, c = queue.popleft()
            current_time = time_map[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < num_row and 0 <= nc < num_column and maps[nr][nc] != 'X' and time_map[nr][nc] == 0:
                    time_map[nr][nc] = current_time + 1
                    queue.append((nr, nc))
        E_time = time_map[E[0]][E[1]]
        L_time = time_map[L[0]][L[1]]
        result.append((L_time, E_time))

    for t in time_map:
        print(t)
    E_time_final = result[0][0] + result[1][1]
    L_time_final = result[0][0]
    if result[0][1] == 0 or result[1][1] == 0 or L_time_final == 0:
        return -1
    return E_time_final

'''
레버까지 갈 수 있지만 최종적으로 출구에 갈 수 있는지도 확인을 해봐야 한다. 그것 떄문에 테스트케이스를 하나 통과하지
못하였었다.
'''
    
