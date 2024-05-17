# 최종 풀이

# 선출선입 구조를 이용하기 위해 큐이용
from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    while truck_weights:
        second += 1
        current_weight -= bridge.popleft()
        if current_weight + truck_weights[0] <= weight: # sum쓰면 5번케이스에서 시간초과 뜸.
            truck_weight = truck_weights.popleft()
            bridge.append(truck_weight)
            current_weight += truck_weight
        else:
            bridge.append(0)
    second += bridge_length
    return second

'''생각할점 or 느낀점
  deque을 통해 queue 자료구조를 사용하여 풀어야된다는 것은 파악했지만, bridge라는 리스트를 선언하여, 현대 다리의 상태를 기록하는 방법은 떠올리지 못했다.

  sum 함수가 시간초과를 발생시킬 수 있는 요소일 수 있다는 것을 깨달았다. sum을 사용하면 매번 bridge만큼의 개수의 수들을 모두 더하기 연산해야한다.
  하지만 현재 bridge의 무게를 기록하는 방식으로 sum을 대신할 수 있다. 결국 sum을 사용하는 이유는 현재 bridge의 총 무게를 구하려고 사용하는 것이기 때문이다.
  더 빨리 풀 수 있도록 연습하자!
'''

# 시도했던 코드

# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
# 다리에 최대 bridge_length대 올라갈 수 있음
# weight 이하 까지의 무게를 견딜 수 있음
# 다리에 완전히 오르지 않은 트럭의 무게는 무시한다
# 트럭 2대가 올라갈 수 있고, 10kg까지 견디는 다리
# 선출선입 구조를 이용하기 위해 큐이용

from collections import deque # 선출선입 구조를 이용하기 위해 큐이용

def solution(bridge_length, weight, truck_weights):
    second = 0
    num_over_trucks = 0
    num_all_trucks = len(truck_weights)
    trucks_on_bridge = deque([])
    truck_weights = deque(truck_weights)
    while num_over_trucks < num_all_trucks:
        print(f'second : {second}, t_on_b : {trucks_on_bridge}, truck_weights : {truck_weights}')
        # 현재 상태에서 트럭이 다리에 진입할 수 있으면
        if not trucks_on_bridge:
            truck = truck_weights.popleft()
            trucks_on_bridge.append(truck)
        elif sum(trucks_on_bridge) + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            trucks_on_bridge.append(truck)
        else:
            trucks_on_bridge.popleft()
        second += 1
    return second

