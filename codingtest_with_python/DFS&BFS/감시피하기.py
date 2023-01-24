# condingtest_with_python_part3_DFS/BFS
# 감시피하기.py

# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 60분, 풀이 시간 : 분 초 )
## BFS인 것 같은데 상하좌우 뿐만이 아니라 장애물 막히기 전까지는 다보니까, 학생뒤에 위치해도 다 뚫어서 봄
## 장애물을 3개 설치해서 선생님의 감시로부터 모든 학생이 피할 수 있는지 계산해야됨
## => 연구소 문제와 비슷하게 완전탐색하고, 선생님한테 들키는 위치에 학생 존재시 False로 하는 함수 구현해야될 듯.
## 
## 인덱스는 1,1 부터 시작
## NxN크기의 복도에서 학생과 선생님의 위치 정보가 주어졌을 때, 장애물을 정학히 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지
## 출력하라
## 근데 연구소 문제와 다르게 숫자를 계싼하는게 아니라 True False만 return하면 되니까 dfs 를 꼭써야할까?
from copy import deepcopy
from itertools import combinations

n = int(input())
# 복도 정보 입력받기
graph = []
temp = [['x'] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(str, input().split())))


# 선생님한테 들키는 지 체크하는 함수

def check():
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 'T':
                # 만약 해당 위치 선생님이라면 상하좌우 장애물을 만날때까지 학생보이나 확인
                # 상
                for r in range(i - 1, -1, -1):
                    if temp[r][j] == 'O':
                        break
                    elif temp[r][j] == 'S':
                        return False
                # 하
                for r in range(i + 1, n):
                    if temp[r][j] == 'O':
                        break
                    elif temp[r][j] == 'S':
                        return False                   
                # 좌   
                for c in range(j - 1, -1, -1):
                    if temp[i][c] == 'O':
                        break
                    elif temp[i][c] == 'S':
                        return False 
                # 우   
                for c in range(j + 1, n):
                    if temp[i][c] == 'O':
                        break
                    elif temp[i][c] == 'S':
                        return False                               
    return True

find = False
Xs = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            Xs.append((i,j))

candidates = list(combinations(Xs, 3))

for candidate in candidates:
    temp = deepcopy(graph)
    for data in candidate:
        r, c = data
        temp[r][c] = 'O'
    if check():
        find = True
        break
      
## 결과 출력
if find:
    print("YES")
else:
    print("NO")
    
"""
dfs 수행
def dfs(count):
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[i][j]
        result = check()
        if result:
            return True
    # 장애물 설치
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                if dfs(count):
                    return True
                graph[i][j] = 'X'
                count -= 1
    return False
r = dfs(0)

"""
# 교재풀이
from itertools import combinations

n = int(input())
board = [] # 복도 정보(N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

## 특정 방향으로 감시를 진행(학생 발견 : True, 학생 미발견 : False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S' # 학생이 있는 경우
                return True
            if board[x][y] == 'O' # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S' # 학생이 있는 경우
                return True
            if board[x][y] == 'O' # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 0:
        while x >= 0:
            if board[x][y] == 'S' # 학생이 있는 경우
                return True
            if board[x][y] == 'O' # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 0:
        while x < n:
            if board[x][y] == 'S' # 학생이 있는 경우
                return True
            if board[x][y] == 'O' # 장애물이 있는 경우
                return False
            x += 1
    return False                        

## 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
        return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

## 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")


# 느낀점
"""
1. 교재에서도 DFS/BFS를 파이썬조합라이브러리를 이용하여 대체했다.
2. 처음에 연구소의 아이디어를 떠올리고 풀어보았으나 무한루프?에 빠진 것인지 결과가 출력되지 않았다.
3. 완전탐색으로 모든 빈공간에 대해 3개의 장애물을 설치하는 경우들을 모두 확인하는 방식으로 풀었다.
4. 장애물을 설치 후 선생님한테 들키지 않는지를 판단하는 함수를 구현할 때, T에서 부터 시작해야되는 것을,
    0부터 n까지 쭉 보게 되도록 코드를 작성해서 틀렸고, 이후에 다시 교재 해설을 통해, 그냥 선생님이 있는 위치에서 부터  반복문으로 상하좌우를
    확인하면 된다는 것을 알게 됐다. 그것빼고는 풀이 아이디어 자체는 교재풀이와 일치하였다.
"""
