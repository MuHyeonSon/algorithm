# condingtest_with_python_part2_DFS&BFS
# 미로탈출.py

## 동빈이의 위치 : (1,1)
## 출구의 위치 : (N,M) ////따라서 맵 인덱스에 접근할 때는 위치에 대한 row와 column 값에 대해 -1 혹은 +1 처리를 해줘야 될 것 같음
## 괴물이 있는 부분 : 0
## 괴물이 없는 부분 : 1

## 입력 : 첫째 줄에 N,M(4 <= N,M <= 200)이 주어짐. 다음 N개의 줄에는 각각 M개의 정수(0혹은1)로 미로의 정보가 주어짐
##         시작 칸과 마지막 칸은 항상 1이다. 
## 출력 : 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다. 

# 나의 풀이

from collections import deque

N,M = map(int,input().split()) # N : 세로, M : 가로

## 맵 정보 입력 받음
Map = []
for i in range(N):
  Map.append(list(map(int,input())))

count = 0 # 움직여야하는 칸의 개수

dx = [0,0,-1,1] # 현재 위치에서 상,하,좌,우 위치를 계산하기 위해 column 값에 대해 더해야하는 값들을 저장할 목록에 대한 리스트
dy = [-1,1,0,0] # 현재 위치에서 상,하,좌,우 위치를 계산하기 위해 row 값에 대해 더해야하는 값들을 저장할 목록에 대한 리스트

def bfs(row,column): # 해당 위치에서 갈 수 있는 모든 위치를 탐색하는 bfs 함수
  if row <= -1 or row >= N or column <= -1 or column >= M: # 넘겨 받은 위치가 맵의 범위를 벗어나는 경우 
    return False
  row -= 1
  column -= 1
  queue = deque() # bfs를 위한 큐 자료구조 선언
  queue.append([row,column])
  print(f'queue : {queue}')
  while queue:
    current_site = queue.popleft() # 큐자료구조에서 아직 방문하지 않았고 갈 수 있는 위치에 대한 좌표 정보를 한 개 꺼냄
    print(f'current_site : {current_site}')
    #print(f'current_site : {current_site}')
    #print(f'current_site[0] : {current_site[0]}')
    #print(f'dy[i] : {dy[i]}')
    for index in range(4): # 상,하,좌,우 4가지 방향에 대해 모두 살펴 봄
      if (0 <= current_site[0] + dy[index] < N)  and (0 <= current_site[1] + dx[index] < M): # 갈 수 있는 위치라면
        if (Map[current_site[0] + dy[index]][current_site[1] + dx[index]] == 1): # 만약 방문하지 않았다면
          queue.append([current_site[0] + dy[index], current_site[1] + dx[index]]) # 그 좌표 정보를 큐에 삽입
          Map[current_site[0] + dy[index]][current_site[1] + dx[index]] = Map[current_site[0]][current_site[1]] + 1 # 해당 위치를 방문 처리 (이전 위치의 원소에 더하기 1 처리)
      for j in range(N):
        print(Map[j]) # bfs를 실행한뒤 맵을 출력해보면 시작위치가 3으로 되어 있는데 분명 2가되는 건 이해가 가는데 왜 3이 나오는지 모르겠다.   
      print("-------------------------------")  
  print(Map[N-1][M-1]) # 처음위치에서 출구까지가기 위해 움직여야 하는 최소 횟수
  for j in range(N):
    print(Map[j]) # bfs를 실행한뒤 맵을 출력해보면 시작위치가 3으로 되어 있는데 왜냐하면 처음시작위치에서 다음 위치의 값이 2가 되고 시작위치의 값은 여전히 1이므로 시작위치의 다음위치에서 접근이 가능함 근데 다음위치의 값이 '2'니까 더하기 1하면 3이 되는 거임


bfs(1,1) 
    
# 나의 풀이 (Product Code)

from collections import deque

N,M = map(int,input().split()) # N : 세로, M : 가로

## 맵 정보 입력 받음
Map = []
for i in range(N):
  Map.append(list(map(int,input())))

count = 0 # 움직여야하는 칸의 개수

dx = [0,0,-1,1] # 현재 위치에서 상,하,좌,우 위치를 계산하기 위해 column 값에 대해 더해야하는 값들을 저장할 목록에 대한 리스트
dy = [-1,1,0,0] # 현재 위치에서 상,하,좌,우 위치를 계산하기 위해 row 값에 대해 더해야하는 값들을 저장할 목록에 대한 리스트

def bfs(row,column): # 해당 위치에서 갈 수 있는 모든 위치를 탐색하는 bfs 함수
  if row <= -1 or row >= N or column <= -1 or column >= M: # 넘겨 받은 위치가 맵의 범위를 벗어나는 경우 
    return False
  row -= 1
  column -= 1
  queue = deque() # bfs를 위한 큐 자료구조 선언
  queue.append([row,column])
  print(f'queue : {queue}')
  while queue: # queue가 빌때까지 (동작과정3)
    current_site = queue.popleft() # 큐자료구조에서 아직 방문하지 않았고 갈 수 있는 위치에 대한 좌표 정보를 한 개 꺼냄
    for index in range(4): # 상,하,좌,우 4가지 방향에 대해 모두 살펴 봄
      if (0 <= current_site[0] + dy[index] < N)  and (0 <= current_site[1] + dx[index] < M): # 갈 수 있는 위치라면
        if (Map[current_site[0] + dy[index]][current_site[1] + dx[index]] == 1): # 만약 방문하지 않았다면
          queue.append([current_site[0] + dy[index], current_site[1] + dx[index]]) # 그 좌표 정보를 큐에 삽입
          Map[current_site[0] + dy[index]][current_site[1] + dx[index]] = Map[current_site[0]][current_site[1]] + 1 # 해당 위치를 방문 처리 (이전 위치의 원소에 더하기 1 처리)
  print(Map[N-1][M-1]) # 처음위치에서 출구까지가기 위해 움직여야 하는 최소 횟수 출력


bfs(1,1) 
    
# 교재 풀이

from collections import deque

## N,M을 공백으로 구분하여 입력받기
n, m = map(int,input().split())
## 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

## 이동할 네 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

## BFS 소스코드 구현
def bfs(x,y):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x,y))
  # 큐가 빌 때까지 반복
  while queue:
    queue = deque((x,y))
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시 
      if nx < 0 or ny < 0 or nx >= n ny > m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
      # 가장 오른쪽 아래까지의 최단 거리 반환
      return graph[n-1][m-1]

## BFS를 수행한 결과 출력
print(bfs(0,0))

# 느낀점

 """
 지금까지 풀어보았던 문제들에서 보통 갈 수 있는 길은 0 갈 수 없는 길은 1 등으로 표시했었는데
 해당 문제의 경우는 반대의 경우였기 때문에 실전에서 이를 헷갈려 잘못 풀 수 있을 수도 있다는 생각을
 하여 항상 문제를 꼼꼼히 읽고 문제를 풀 때에도 문제에서 주어지는 내용들을 잘 기억하며 코드를 작성해야겠다고 생각했다.
 또한 최단거리문제와 미로탈출문제에서 탈출을 위한 칸의 개수를 구하는 것이 어떠한 차이가 있을까에 대해서도 생각해보고
 최단거리문제는 아직 해당 책을 학습하며 다루지 않았기 때문에 잘 기억하고 있어야 겠다고 생각했다.
 또한 나는 이문제를 풀기 전에 DFS와 BFS에 동작과정과 동작방식에 대해 정확하게 이해하지 못하고 있었다는 것을
 알게되어 교재를 다시 정독하고 동작방식을 직접 적어보며 이해를 하는 것을 먼저 진행하였다.
 그럼에도 잘 이해가 되지 않지만 복습과 반복만이 살 길이라고 생각하며 했다.
 또한 교재와의 풀이를 비교해보며 내가 작성한 코드는 이전 큐 함수 구현한 것을 거의 응용하여 풀었기 때문에
 전체 코드 line수 자체는 더 짧지만 line 한 줄의 길이가 너무 길고 복잡해서 직관적으로 잘 알아보기가 비교적 더 힘들다고 느꼈다.
 x y 자체가 가로축세로축이랑 헷갈려서 이것에 대한 차이는 내가 편한대로 구현해도 상관 없다고 생각하지만 코드의 간결함의 차이가
 너무 심하게 차이가 난다고 생각하였고 실전에서도 교재 풀이와 같이 푸는 것이 문제가 생겼을 때 코드를 빠르게 수정하는데 더 용이하다고
 생각하여 교재의 코드를 따라가는 것이 좋다고 생각하였다.
 """
