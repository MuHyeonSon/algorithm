# condingtest_with_python_part2_DFS&BFS
# 음료수얼려먹기.py

# 나의 풀이

from compliments import deque
queue = deque()

def bfs(graph,start,visited):
  queue.append(start)
  visited[start] = True
  while queue:
    Node = queue.popleft()
    for adjacent_node in Node:
      if not visited[adjacent_node]:
        queue,append(adjacent_node)
        visited[adjacent_node] = True      

N,M = map(int,input().split()) # N : 세로 길이, M : 가로 길이
graph = []

## 얼음 틀 형태 입력 받기
for i in range(N):
  row = []
  input_row = input()
  for element in input_row:
    row.append(element)
  graph.append(row)

## 0의 conneted component 찾아내기
visited = [False] *(N*M) 

for i in range(N):
  for j in range(M):
    b = 0
    
# 나의 풀이 (Product Code)
    
N,M = map(int,input().split())

ice_frame = []

# 얼음틀 형태 (맵) 정보 입력받기
for i in range(N):
  ice_frame.append(list(map(int,input()))) #### 여기서 컴마나 공백으로 구분안해도 문자열이 알아서 split 돼서 하나의 문자열이 하나의 원소로 들어감####

def dfs(x,y):
  if x <= -1 or x >= N or y <= -1 or y >= M: # 얼음틀 형태의 인덱스 범위 바깥을 접근하면 False
    return False
  if ice_frame[x][y] == 0: # 0이면 (구멍이 뚫려있는 부분이면, 즉 아직 방문하지 않은 곳이면)
    ice_frame[x][y] = 1 # 방문 처리
    # connected component (노드 묶음)의 원소 찾기 위해 상하좌우 살핌 (문제에서 구멍이 뚫려있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것이라고 했기 때문)
    dfs(x-1, y) # 상
    dfs(x+1, y) # 하
    dfs(x, y-1) # 좌
    dfs(x, y+1) # 우
    return True # 0이면 하나의 아이스크림이므로 True 리턴
  return False # 0이 아니면 False

count_of_icecream = 0

for i in range(N):
  for j in range(M):
    if dfs(i,j): # i,j번째 위치가 구멍이 뚫려 있는 부분이라면 아이스크림이 생성되므로
      count_of_icecream += 1 # 전체 얼음틀에서 아이스크림의 개수에 대한 카운트에 하나를 더함

print(count_of_icecream) # 총 아이스크림의 개수 출력

# 교재 풀이

# 느낀점 
 """
 앞서 정의한 큐를 이용한 BFS나 스택을 이용하는 DFS를 이용하면 되는 줄 알았는데 
 교재의 풀이를 보면서 DFS를 하는 것 까지는 이해가 갔는데 스택 자료구조를 이용하지 않고
 문제에 맞게 푼 듯한 답안을 보고서 아니 고정적인 알고리즘 코드와 자료구조가 있는 것이 아니라는 것을
 알게 되었다.. DFS와 BFS가 어떠한 탐색방식인지를 잘 알고 있고 이용하는 방법에 익숙해지는 것이 중요하다고
 생각하여 가장 처음에 정의된 그래프 탐색을 위한 DFS와 BFS 함수를 외우는 것이 큰 의미가 없다는 생각을 하였다.
 더 많은 문제를 풀어봐야 더 잘 알게 될 수 있겠지만 처음부터 응용문제와 같은 문제가 나와서 당황스러웠다.
 그리고 앞서 정의된 함수를 이용하여 구현하려다보니 도대체 어떻게 이문제를 푸는게 가능한지 헷갈리며
 시간도 낭비했다고 생각듫지만 그만큼 더 머릿속에 각인될 것 같다.
 """
