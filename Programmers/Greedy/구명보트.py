# 한번에 최대 2명씩 탈 수 있음
# 무게 제한 있음
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값
#  0 < len(people) < 50,000
# 일단 몸무게 순으로 정렬시킨 뒤,
# 가장 작은 사람과 가장 큰사람의 몸무게를 합하여 (2명이니까) 제한무게 넘는지 확인하고
# 넘는다면 큰 사람만 먼저 태우고, 작은 사람은 다음 차례까지 대기시키자

def solution(people, limit):
    result = 0
    start = 0
    people.sort()
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        result += 1    
    return result

'''생각할 점 및 느낀점
남은 사람들 중 몸무게가 가장 큰 사람과 작은 사람을 선택해야할 것이라는 것은 떠올렸으나, 2명만 태울 수 있다는 부분을 제대로 인지하지 못하여
한참 헤맸다. 문제를 다음엔 더 꼼꼼히 읽도록 하고, 그리디 문제를 더 많이 풀어봐야 겠다는 것을 느낄 수 있었다.
'''
''' sol 1) => 실패
from collections import deque
import heapq
from deepcopy import copy

def solution(people, limit):
    answer = 0
    people.sort()#reverse=True)
    people_queue = deque(people)
    print(people_queue.pop())
    print(people_queue.popleft())
    #print(people)
    #min_1 = heapq.heappop(people)
    #print(people)
    #min_2 = heapq.heappop(people)
    #print(people)
    #print(f'min_1 : {min_1}, min_2 : {min_2}')
    while people_queue:
        temp = deepcopy(people_queue)
        if len(people_queue) > 2:
            if min_num
            min_num = people_queue.popleft()
            max_num = people_queue.pop()
            answer += 1
        else:
            people_queue.popleft()
            answer += 1
    """
    while people:
        print(people)
        temp_sum = 0
        for _ in range(len(people)):
            p = people.pop()
            if temp_sum + p > limit:
                people.append(p)
                break
            temp_sum += p
        answer += 1
    """
    return answer
'''
