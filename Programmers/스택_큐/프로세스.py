# 프로그래머스 스택/큐 프로세스.py

from collections import deque

def solution(priorities, location):
    terminated_processes = []
    queue = deque([(index, priority) for index, priority in enumerate(priorities)])
    index = 0
    while queue:
        prio = queue.popleft()
        if any([prio[1] < priority for index, priority in queue]):
            queue.append(prio)
        else:
            terminated_processes.append(prio)
    for terminated_process in terminated_processes:
        if terminated_process[0] == location:
            return terminated_processes.index(terminated_process) + 1

  ''' 느낀점 또는 생각할 점
  문제는 간단해 보였지만, 처음에 인덱스에 대한 정보를 따로 주기 위해 각 프로세스의 위치정보를 기록할 리스트를 만들었으나,
  종료한 프로세스는 그자리에 두고 그 다음 두 번째 인덱스부터 pop을 해야되는 작업을 어떻게 구현해야될지 해결하지 못했다.
  
  다른 풀이를 찾아보니, enumerate를 사용해 위치정보와 우선순위정보를 함께 갖고 있는 튜플로 구성된 리스트를 큐자료구조로서 만들었다.
  => 이것으로 다음 두 번째 인덱스부터 pop을 해야되는 작업 문제를 해결할 수 있었다.

  자료구조를 이루는 한 데이터가 값이 하나라면 max를 통해 현재 값보다 더 큰 값을 가진 수가 있는지 찾을 수 있지만, 선언한 queue가 2차원 형태의 튜플이므로
  max를 사용하지 못했다. any라는 함수를 통해 두번째 인덱스 값들 중 현재 꺼낸 값보다 큰 값이 있는지(우선순위가 더 높은 프로세스가 있는지) 여부를 판단할 수 있었다.  
  '''
