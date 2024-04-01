''' 느낀점 or 생각해볼점
각 배포마다 몇 개의 기능이 배포되는지를 return 해야된다는 것은 쉽게 이해하였지만, 실제적으로 어떻게 돌아가야되는지
파악하기 위해, 예시를 빠르게 적어보면서, 알고리즘을 떠올릴 수 있었다. progresses의 순서대로 배포를 해야하고, 배포된 작업을 pop한 뒤
배포된 작업의 개수를 구해야하기 때문에 자연스럽게 deque 자료구조를 떠올렸다. 또한 계산을 쉽게 하기 위해 progresses 각 원소에 대응되는 speeds를 이용하여
배포 가능한 남은 일 수를 계산하여 현재 가장 앞에 위치한 task의 남은 기간보다 적게 걸리는 것들은 모두 한 번에 제거해도 됨을 떠올려, 이를 코드로 작성하니
문제가 풀렸다. 기억해야될 점은, 데이터를 popleft한 뒤, 다음 데이터보다 작다면 다시 큐에 넣어야하며 이때 append가 아닌 appendleft를 사용해야 함에 주의해야겠다.
사실 후입선출 방식이 필요하기 때문에 stack 자료구조를 사용하는 것이 더 적절하였을지 모른다. stack 구조를 사용했더라면 데이터를 거꾸로 뒤집어야 한다.

제일 아쉬운점은 풀이시간이다. 지금보다 훨씬 빨리 풀어야한다. 아직 느려도 조금씩 문제들이 풀리기 시작하고 속도도 개선되고 있다. 할 수 있다!!
'''

# 각 배포마다 몇 개의 기능이 배포되는지를 return
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    expected_days = deque([]) # 큐자료구조를 이용(자료구조의 앞 위치에서 추가하고 빼야되므로)
    for i in range(len(progresses)):
        expected_day = 0
        left_time = 100 - progresses[i]
        expected_day = math.ceil(left_time / speeds[i])
        expected_days.append(expected_day)
    while expected_days:
        current_num_release = 1
        current_task = expected_days.popleft()
        if len(expected_days) == 0:
            answer.append(current_num_release)
            break
        while expected_days:
            next_task = expected_days.popleft()
            if next_task > current_task:
                expected_days.appendleft(next_task)
                break
            current_num_release += 1
        answer.append(current_num_release)
    return answer
