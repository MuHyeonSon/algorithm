# condingtest_with_python_part3_DFS/BFS
# 블록이동하기.py

# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 50분, 풀이 시간 : 1시간 30분 초 )
## 1,1 부터 인덱스 시작
## 0 은 빈칸, 1은 벽
## 로봇은 앞뒤로 이동 가능, 회전 가능(90도씩 회전 가능)
## 로봇의 두부분 중 어느 한 어느 칸이든 축이 될 수 있음
## 로봇이 차지하는 두 칸 중 어느 한 칸 이라도 N, N 위치에 도착하면 됨
## 한 칸 이동하거나 90도 회전 하는데 걸리는 시간은 정확히 1초임
## 로봇이 N,N까지 이동하는데 필요한 최소 시간을 구하라
## 파트2 미로탈출 문제와 유사한데 bfs이용했고, 각 노드에다가 이전 노드 + 1한 값 더한 값으로
## 저장했고 그래프 두 개 만들었음.
## 근데 90도 회전하는게 카카오 열쇠문제처럼 풀어야되나???,,
from collections import deque
#from copy import deepcopy

def solution(board):
    n = len(board) - 1
    answer = 0
    #graph = deepcopy(board)
    # 방향 벡터 정의
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 90도 회전 방향벡터 정의 왼쪽 부분을 뒤로 혹은 앞으로, 오른쪽부분을 뒤로 혹은 앞으로
    # 가로로 있을 때 왼쪽 시계 90도 왼쪽 반시계 90도 오른쪽 시계90도 오른쪽 반시계 90도전부
    x_rr = [(1,0), (-1,0), (0,1), (0, -1)] #(왼쪽, 오른쪽) 
    x_rc = [(1,0), (1,0), (0,-1), (0, -1)]
    # 세로로 있을 때 위쪽 시계 90도 아래쪽 반시계 90도 위쪽 시계90도 아래쪽 반시계 90도전부
    y_rr = [(1,0), (1,0), (0,-1), (0,-1)] #(위쪽, 아래쪽)
    y_rc = [(-1,0),(1,0), (0,-1), (0,1)]
    start = ((0,0),(0,1), 'x')
    q = deque()
    q.append(start)
    board[start[0][0]][start[0][1]] += 1
    board[start[1][0]][start[1][1]] += 1
    
    while q:
        left, right, direction = q.popleft()
        left_r, left_c = left
        right_r, right_c = right
        if direction == "x":
            if right_c < left_c:
                left_r, left_c, right_r, right_c = right_r, right_c, left_r, left_c
        # 두 부분 중 r이 더 작은 것을 위쪽으로 정할 거임 (위쪽을 왼쪽으로 정했으니까왼쪽r이 더 작아야됨 그것도 맞춰줌)
        elif direction == "y":
            if right_r < left_r:
                left_r, left_c, right_r, right_c = right_r, right_c, left_r, left_c
        for i in range(4):
            nleft_r = left_r + dr[i]
            nleft_c = left_c + dc[i]
            nright_r = right_r + dr[i]
            nright_c = right_c + dc[i]    
            if 0 <= nleft_r <= n and 0 <= nleft_c <= n and 0 <= nright_r <= n and 0 <= nright_c <= n:
                if board[nleft_r][nleft_c] == 0 and board[nright_r][nright_c] == 0:
                    board[nleft_r][nleft_c] = board[left_r][left_c] + 1
                    board[nright_r][nright_c] = board[right_r][right_c] + 1
                    q.append(((nleft_r, nleft_c), (nright_r, nright_c), direction))
        if direction == 'x':
            for i in range(4):
                nleft_r = left_r + x_rr[i][0]
                nleft_c = left_c + x_rc[i][0]
                nright_r = right_r + x_rr[i][1]
                nright_c = right_c + x_rc[i][1]    
                if 0 <= nleft_r <= n and 0 <= nleft_c <= n and 0 <= nright_r <= n and 0 <= nright_c <= n:
                    if board[nleft_r][nleft_c] == 0 and board[nright_r][nright_c] == 0:
                        board[nleft_r][nleft_c] = board[left_r][left_c] + 1
                        board[nright_r][nright_c] = board[right_r][right_c] + 1
                        q.append(((nleft_r, nleft_c), (nright_r, nright_c), 'y'))                    
        if direction == 'y':
                nleft_r = left_r + y_rr[i][0]
                nleft_c = left_c + y_rc[i][0]
                nright_r = right_r + y_rr[i][1]
                nright_c = right_c + y_rc[i][1]    
                if 0 <= nleft_r <= n and 0 <= nleft_c <= n and 0 <= nright_r <= n and 0 <= nright_c <= n:
                    if board[nleft_r][nleft_c] == 0 and board[nright_r][nright_c] == 0:
                        board[nleft_r][nleft_c] = board[left_r][left_c] + 1
                        board[nright_r][nright_c] = board[right_r][right_c] + 1
                        q.append(((nleft_r, nleft_c), (nright_r, nright_c), 'x'))    
    for i in range(n+1):
        for j in range(n+1):
            print(board[i][j], end = " ")
        print()
    answer = board[n][n]            
    return answer

# 교재 풀이

from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과(이동 가능한 위치들)
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
            
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            # 왼쪽 혹은 오른쪽 두칸이 모두 비어 있다면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
                
        
    # 현재 로봇이 세로로 놓여 있는 경우
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            # 위쪽 혹은 아래쪽 두칸이 모두 비어 있다면
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외각에 벽을 두는 형태로 맵변환
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달 했다면, 최단 거리이므로 반환
        if (n, n) in pos: # 한 부분이라도 도달했다면
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고, 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

# 느낀점
"""
part2의 미로탈출 문제와 굉장히 비슷하였다. 다른 점은 로봇이 차지하는 칸이 두칸이라는 점과, 회전을 통해 이동할 수 있다는 점이다.
그래서 미로탈출의 풀이 아이디어를 그대로 사용하되 로봇이 두 칸이라는 점과 회전을 통해 이동한다는 점을 고려하여
코드를 작성하였다. 풀이시간 50분을 넘기고 1시간 반가까이 풀어 제출해봤지만 테스트케이스를 통과하지 못했고,
기대한 것과 다르게 동작하였다. 문제 해설을 보았을 때, 미로탈출 과는 조금 다른 방식으로 풀었고 핵심은 다음과 같았다.

1. 로봇이 차지하고 있는 위치가 두칸임으로 위치 정보를 튜플로 처리하여, 방문 여부를 관리하고,
    
2. 로봇의 상태를 집합 자료형(set)으로 관리한다. 집합 자료형을 이용해 관리하면 한 번 방문한(큐에 들어간) 로봇의 상태는 두번 방문 하지 않음

3. 초기에 주어진 맵을 변형해서 외곽에 벽을 두면 로봇이 맵을 벗어나지 않는지, 범위 판정을 더 간단히 할 수 있음

4. 특정한 위치에서 이동 가능한 다음 위치를 반환하는 get_next_pos() 함수를 구현함.

5. q에 넣는 정보는 다음 이동할 위치와 cost + 1 이며, 처음 초기화할 땐, 현재 위치와, cost를 0으로 설정한다 ({(1,1),(1,2)}, 0) # 외곽추가때문에 1,1 부터 시작 (문제에서도 1,1부터고)

6. 상하좌우, 가로로 놓여있는 경우에 위쪽 회전 아래쪽 회전 모두 고려했는데 교재 풀이가 정말로 깔끔했다.. 장황하게 코드를 작성하지 않고,
    회전시 가로로 놓여있는 경우 위로 회전과 아래로 회전, 세로로 놓여잇는 경우 왼쪽 회전과 오른쪽회전 두가지로 구분하여 그냥 pos1_x, pos1_y pos1_x + 1 pos1_y 이런식으로
    엄청 간단하게 표현하였다. 그냥 회전 결과가 왼쪽과 오른쪽 중 하나에 대해 1 빼거나 1더한 위치만큼 다른 하나를 이동하면 끝나기 떄문에 매우 간편했다. 
    
7.     # 현재 로봇이 가로로 놓여 있는 경우
    if post1_x == post2_x:
        
    # 현재 로봇이 세로로 놓여 있는 경우
    if post1_y == post2_y:
        이런식으로 가로 세로를 깔끔하ㅔ 구분하였다.
"""
