# condingtest_with_python_part3_구현
# 뱀.py

# 나의 풀이 (교재 해설 참고)

# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 분 초)
## 뱀은 매초마다 이동
## 게임 시작 시 맨 위 맨 좌측 (0,0)에 위치
## 처음에 오른쪽을 향함

from collections import deque

## 게임이 몇 초에 끝나는 지를 담을 변수
result_time = 0

## 보드(N*N)의 크기 입력받기
n = int(input())
board = [[0]*n for _ in range(n)] 
board[0][0] = 1 # 뱀의 첫 위치

## 사과의 개수 입력 받기
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    board[a][b] = 2 # 사과 : 2

## 방향 변환 횟수 입력 받기
l = int(input())
transform = deque([])
for i in range(l):
    # x초 후에 c(L(완쪽) or D(오른쪽)) 로 변환
    X, C = map(str, input().split())
    transform.append((int(X), C))

## 방향벡터 정의
## 상하좌우 순으로 각각의 방향에 대해 앞으로 직진했을 때 필요한 연산 숫자
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

## 방향정의 (0:상,1:하,2:좌,3:우)
d = 3
# 방향정보를 표시하는 d를 바꾸기 위한 함수
def turn_direction(direction):
    global d
    # 현재 방향이 오른쪽이라면
    if d == 3:
        if direction == 'L':
            d = 0
        elif direction == 'D':
            d = 1
    elif d == 0:
        if direction == 'L':
            d = 2
        elif direction == 'D':
            d = 3
    elif d == 1:
        if direction == 'L':
            d = 3
        elif direction == 'D':
            d = 2
    elif d == 2:
        if direction == 'L':
            d = 1
        elif direction == 'D':
            d = 0  

snake = deque([(0,0)])
r = 0
c = 0

for i in range(n):
    for j in range(n):
        print(board[i][j], end = " ")
    print()

while True:
    if len(transform) > 0 and transform[0][0] == result_time:
        print(transform)
        turn_direction(transform[0][1])
        print(f'd : {d}')
        transform.popleft()
        print(transform)
    nr = r + dr[d]
    nc = c + dc[d]
    # 만약 갈 수 있는 곳이라면 (보드 범위 벗어나지 않고 자기자신의 몸과 부딪히지 않으면)
    print(f'nr : {nr}, nc : {nc}')
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print()    
    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1:
        # 만약 다음칸에 사과위치해 있으면
        if board[nr][nc] == 2:
            snake.append((nr, nc)) # 몸길이를 늘린다. (즉, 꼬리를 움직이지 않음)
            board[nr][nc] = 1
            r = nr
            c = nc

        # 사과가 없다면
        else:
            a, b = snake.popleft() #snake가 위치한 곳에서 꼬리 빼고
            snake.append((nr, nc)) # 다음칸에 머리 위치 시킴
            board[a][b] = 0
            board[nr][nc] = 1
            r = nr
            c = nc
        result_time += 1
    else:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end = " ")
            print()
        result_time += 1
        break


print(result_time)

# 나의 풀이(최종)

from collections import deque

## 게임이 몇 초에 끝나는 지를 담을 변수
result_time = 0

## 보드(N*N)의 크기 입력받기
n = int(input())
board = [[0]*n for _ in range(n)] 
board[0][0] = 1 # 뱀의 첫 위치

## 사과의 개수 입력 받기
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    board[a][b] = 2 # 사과 : 2

## 방향 변환 횟수 입력 받기
l = int(input())
transform = deque([])
for i in range(l):
    # x초 후에 c(L(완쪽) or D(오른쪽)) 로 변환
    X, C = map(str, input().split())
    transform.append((int(X), C))

## 방향벡터 정의
## 상하좌우 순으로 각각의 방향에 대해 앞으로 직진했을 때 필요한 연산 숫자
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

## 방향정의 (0:상,1:하,2:좌,3:우)
d = 3
# 방향정보를 표시하는 d를 바꾸기 위한 함수
def turn_direction(direction):
    global d
    # 현재 방향이 오른쪽이라면
    if d == 3:
        if direction == 'L':
            d = 0
        elif direction == 'D':
            d = 1
    elif d == 0:
        if direction == 'L':
            d = 2
        elif direction == 'D':
            d = 3
    elif d == 1:
        if direction == 'L':
            d = 3
        elif direction == 'D':
            d = 2
    elif d == 2:
        if direction == 'L':
            d = 1
        elif direction == 'D':
            d = 0  

# 뱀이 차지하는 영역에 대한 인덱스들을 담는 큐 선언, 뱀의 머리에 처음위치 설정
snake = deque([(0,0)])
r = 0
c = 0

# 게임 시작
while True:
    if len(transform) > 0 and transform[0][0] == result_time:
        turn_direction(transform[0][1])
        transform.popleft()
    nr = r + dr[d]
    nc = c + dc[d]
    # 만약 갈 수 있는 곳이라면 (보드 범위 벗어나지 않고 자기자신의 몸과 부딪히지 않으면)
    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1:
        # 만약 다음칸에 사과위치해 있으면
        if board[nr][nc] == 2:
            snake.append((nr, nc)) # 몸길이를 늘린다. (즉, 꼬리를 움직이지 않음)
            board[nr][nc] = 1
            r = nr
            c = nc
        # 사과가 없다면
        else:
            a, b = snake.popleft() #snake가 위치한 곳에서 꼬리 빼고
            snake.append((nr, nc)) # 다음칸에 머리 위치 시킴
            board[a][b] = 0
            board[nr][nc] = 1
            r = nr
            c = nc
        result_time += 1
    else:
        result_time += 1
        break


print(result_time)


# 느낀점
"""
내가 실수해서 시간을 엄청 많이 잡아먹은 점. (앞으로 구현 문제에서 뭔가가 막혔다면 이것들을 꼭 제데로 신경썼는지 확인할 것.)
    1. 1,1부터 시작인 걸 고려하지 못했음 (인덱스 범위 잘 확인 하기)
    2. =이랑 == 잘못쓰는 실수를 범함
    3. 사과 없을 때 꼬리 부분을 0으로 바꿔줘야되는 걸 인덱스값 잘못설정함.
    
확실히 짚고 넘어가야될 점.    
    1. 함수에서 파라미터는 전역변수로 쓸 수 없다.
"""

"""
📰 Codingtest_with_python_part3_구현_뱀
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 구현 문제 풀이 느낀점
"""
