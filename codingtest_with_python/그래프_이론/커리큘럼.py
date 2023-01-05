# condingtest_with_python_part2_그래프이론
# 커리큘럼.py

# 나의 풀이 (주어진 풀이 시간 : 50분, 풀이 시간 : 1시간 18분 31.28초)
## "선수 강의", "수강하기까지 걸리는" -> 방향이 있는 그래프에서 방향에 따라 순차적으로 노드를 방문하는 위상정렬 알고리즘을 사용
## 해야겠다고 생각 

## 위상정렬 (deque라이브러리를 통해 queue를 사용)
## 0. 진입차수가 0인 노드들을 모두 큐에 넣는다.
## 1-1. 큐에서 노드를 꺼내 해당 노드에서 시작되는 간선 모두 제거
## 1-2. 새롭게 진입차수가 0이된 노드들을 모두 큐에 넣는다.
## 2. 큐가 빌 때까지 반복 (만약 모든 노드를 방문하기 전에 큐가 빈다면 사이클이 있는 것.)

from collections import deque
## 강의의 수 입력받기 (노드 수 입력 받기)
N = int(input())
## 진입 차수 테이블 선언 및 초기화
indegree = [0] * (N + 1)
time_table = [0] * (N + 1)
#graph = [[] for i in range(N)]
graph = [0] * (N + 1)

# # 다 넣는 게 아니라 최소 시간인 애를 넣어야 됨
for i in range(1, N + 1):
  lecture = list(map(int, input().split()))
  t = lecture.pop(0) # 강의 시간 정보 추출
  lecture.remove(-1) # -1 제거
  time_table[i] = t
  if len(lecture) != 0:
    # lecture에는 i 강의의 선수강의 들의 번호만 남음 (선수 강의들 중 시간이 가장 작은애를 선택해서 그것만 남겨야됨)
    min_time_lecture  = lecture[0]
    for j in lecture:
      # 입력 받은 강의의 시간이 해당 강의 다음으로 듣는 강의들보다 강의 시간이 가장 작다면
      if (time_table[j] != 0) and (time_table[j] < time_table[min_time_lecture]):
        min_time_lecture = j
    # i번째 강의를 N개의 강의를 최소시간으로 수강하기 위한 커리큘럼에 입력받은 강의의 선수 강의로 선정
    graph[min_time_lecture] = i
    indegree[b] += 1  


def topology_sort():
  # N개의 강의에 대해 수강하기까지 걸리는 최소시간을 담을 변수 선언
  result = 0
  q = deque()
  ## 진입 차수가 0인 노드를 모두 큐에 넣음
  for i in range(1,N+1):
    if indegree[i] == 0:
      q.append(i)
  # 큐가 빌 때까지
  while q:
    node = q.popleft()
    # 큐에서 노드를 꺼내 그 노드에서 시작되는 간선 제거
    i = graph[node] # 해당 노드가 가리키는 노드
    indegree[i] -= 1
    # 만약 그 노드의 진입 차수가 0이라면
    if indegree[i] == 0:
      # 큐에 넣는다
      q.append(i)
      result += time_table[i]
  
  # N개의 강의에 대해 수강하기까지 걸리는 최소시간 출력
  print(result)    

topology_sort()


# 나의 풀이 (교재 해설 참고)

from collections import deque
import copy

## 노드의 개수 입력받기
N = int(input())
## 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N + 1)
## 각 노드에 연결된 간선정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(N + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (N + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, N + 1):
  data = list(map(int,input().split()))
  time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있기 때문에 0번째인덱스 값을 강의시간 정보 리스트에 반영
  for node in data[1:-1]: # 가장 마지막원소의 인덱스가 -1이고 실제 값도 -1인데 -1로 그 노드 정보를 끝내는 거였으니까
    graph[node].append(i) # i의 선수 과목이 node라는 걸 그래프에 반영
    indegree[i] += 1 # 진입 차수 1 증가

# 위상 정렬 함수
def topology_sort():
  result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, N + 1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌 때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    # 해당 원소와 연결된 노드들에 대한 간선을 끊음(진입차수 -1 했다는 것)
    for i in graph[now]:
      # 교재에서 설명이 부족하다고 느꼈음.. 내가 이해한 것으로는 강의를 동시에 여러 개 들을 수 있고,
      # 선수과목이 여러개면 여러 개 다 들어야 되니까, 여러 개의 과목 중 가장 큰 값은 나머지 강의들의 시간들을 모두 포괄할 수 있으므로
      # max 값을 선택하는 것이라고 이해했음
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1 ########################
      # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  # 위상 정렬을 수행한 결과 출력
  for i in range(1, N + 1):
    print(result[i])

topology_sort()


# 교재 풀이




# 느낀점
"""
풀 수 있을 것 같다고 생각하여 시간을 더 투자하였지만
시간을 초과하고 마지막시도를 했을 때 원하는 결과가 나오지 않아 여기서 멈추었다.
해설을 봐도 이해가 안가서 직접 노트에 각 변수와 리스트들의 상태, 그래프 상태를 전부 그려보며
이해하려고 해도 몇 시간이 걸리고 구글에 검색 해봐도 바로 이해가 가지 않았다.
내가 이해가 가지 않았던 부분은 왜 현재 처리하고 있는 노드의 인접노드의 최소 시간을 업데이트할 때,
그 인접노드의 최소시간, 그리고 현재 처리하고 있는 노드의 강의 시간과 인접노드의 강의시간을 더한 값 중
더 큰 시간을 선택하여 그 인접노드의 최소시간정보를 업데이트하는 것인지 이해가 가지 않았다.
왜 둘 중 max값을 선택하는지 이해가 가지 않았고, 큰 값으로 결정하는 것이 더 적은 시간이 걸리는
강의를 포괄하기 때문이라는 것을 읽고, 그말조차 이해가 가지 않았는데,
문제에서 동시에 강의를 들을 수 있다는 점을 고려해보니, 그냥 최소 시간이라는 게 여러 개의 강의들이 있을 때,
선수강의 정보를 고려하여, 순서대로 나열하는 것을 말하는 것이라는 걸 알게 되었다.
최소시간이 들게 하려면 선수강의는 무조건 들어야 하니까,
나는 선수강의가 여러 개가 있으면 그 중 가장 시간이 적은 선수 강의를 선택해서 듣는 것을 말하는 게 아니었나
하는 생각에 계속 이해를 하지 못했던 것이다. 지금 새벽 몇 시인지 시계를 보기조차 짜증나게 시간이 많이 지났다.
달콤커피 카페에서 저녁 7시쯤부터 풀고 도서관에서 40분 정도 더 보고, 집에 와서
해설을 보고 바로 정리를 하려고 했던 것인데 이렇게 까지 시간과 에너지가 들어갈 거라고 생각하지 못했고, 
그래프이론문제가 꼭 알고있어야 된다고 하지만, 다른 유형들에 비해 비중도 낮고 시험도 얼마 안남은 상황에서
이렇게 .. 하...조금만 더 적으면 욕설을 적을 것 같아서 그냥 여기까지 써야겠다..*(&^*&^*&^*
"""
