# condingtest_with_python_part3_Greedy
# 무지의먹방라이브.py



# 나의 풀이 (교재 해설 참고)
## 해설에서 설명하는 우선순위큐를 사용한다는 점과 먹는 시간이 작은 음식부터 처리한다는 아이디어만을 고려하여 구현 
## 해설에서 설명하는 우선순위큐를 사용한다는 점과 먹는 시간이 작은 음식부터 처리한다는 아이디어만을 고려하여 구현 

import heapq

def solution(food_times, k):
    # k초 내의 다 먹을 수 있는 경우 k초 후에 더 먹을 음식이 없으므로 -1 반환
    if sum(food_times) < k:
        return -1
    q  = []
    x = 4
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    for i in range(min(food_times), max(food_times) + 1):
        if k > food_times[food_times.index(i)]:
            print(f'i : {i}')
            print(f'food_times.count(i) : {food_times.count(i)}')
            for j in range(food_times.count(i)):
                heapq.heappop(q)
                k -= 1
        # 만약 현재 가장 작은 시간을 소요하는 음식을 먹는 시간이 남은 k초보다 더 크다면
        # i부터 순차대로 하나씩 먹기
        else:
            print("asdasd")
            x = food_times.index(i)
            for _ in range(k):
                x += 1
                if x > (len(food_times) - 1):
                    x = 0
            break
        
    answer = x + 1
    return answer
### ====================> 결과 runtime error



# 나의 풀이 (주어진 풀이 시간 :30 분, 풀이 시간 : 50분 초)
## 네트워크 정상화 후 다시 방송을 이어갈때 네트워크 장애가 발생한 시간 k초를 고려하여
## 몇 번 음식부터 다시 섭취하면 되는지 return하기

def solution(food_times, k):
    if sum(food_times) == 0:
        return -1
    
    order = 0
    #max_order = len(food_times) - 1
    for _ in range(k):
        if food_times[order] == 0:
            order = (order + 1) % len(food_times)
            for i in range(order, order + len(food_times)):
                i = i % len(food_times)
                if food_times[i] > 0:
                    order = i
                    break
        if food_times[order] <= 0:
            return -1
        else:
            food_times[order] -= 1
            order = (order + 1) % len(food_times)
    answer = order + 1
    return answer

# 교재 풀이
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1 반환
    if sum(food_times, k):
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = 0 # 남은 음식의 개수
    
    # sum_value + ((현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k를 비교
    while sum_value + q((q[0][0] - previous) * length) <= k:
        now heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length += 1
        previous = now # 이전 음식 시간 재설정
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x : x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
    
    answer = 0
    return answer



# 느낀점
"""
진심으로 이런 문제를 그리디로 풀생각을 하려면 얼마나 많이 풀어봐야 하는 건가?,, 라는 생각이 들게 만드는 문제였다.
해설을 보고 문제의 풀이법이 잘 이해가 가지 않아 문제 풀이법을 먼저 이해하고 향후 그리디 문제 리뷰를 할 때 이 문제는 무조건
다시 풀이법을 완전히 이해하여 구현할 때까지 필수적으로 보고 그 뒤로도 잊지않도록 계속해서 봐야겠다고 생각했다.

새로 알게된 점은 다음과 같다.
1. 우선순위큐를 구현할 때에 heapq의 구조는 원소의 가장 첫번째 원소가 가장 작은 것을 맨 앞으로 가져올 뿐이고 나머지 데이터는 push한 순서대로 위치해 있다.
"""
