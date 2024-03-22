import heapq

# sol2) 통과
# 어차피 가장 마지막에는 원소 하나만 남게 되는데, 그것이 k보다 작다면 -1 return
# 가장 작은 원소 두 개를 뽑을 것이므로 우선순위큐 자료구조를 사용하기 위해 heapq
def solution(scoville, K):
    result = 0
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2 and scoville[0] < K:
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        heapq.heappush(scoville, first_min + (second_min * 2))
        count += 1
        if len(scoville) > 0 and scoville[0] >= K:
            return count
    if scoville[0] < K:
        return -1
    return count

''' sol1) 실패 정확성: 83.9, 효율성: 0.0

import heapq
# 스코빌 지수 >= k 로 만들고 싶음
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# heapq를 사용하여 우선순위큐를 사용하면 맨 앞에 가장 작은수와 그다음으로 작은 수 위치
# 중간에 값
# 나머지는 그냥 원래 순서대로 위치하게 됨

def solution(scoville, K):
    answer = 0
    num = len(scoville)
    scoville.sort()
    while len(scoville) > 1:
        if answer > num - 1:
            break
        # 만약 모든 음식의 스코빌 지수가 K이상이면
        if len([x for x in scoville if x >= K]) == len(scoville):
            return answer
        no_spicy1 = heapq.heappop(scoville)
        no_spicy2 = heapq.heappop(scoville)
        heapq.heappush(scoville, no_spicy1 + (no_spicy2 * 2))
        answer += 1
    if scoville[0] < K:
        return -1
    return answer
'''


''' 생각할 점 or 느낀점
첫 풀이는 정답이 나오게는 풀었지만 효율성 테스트에서 0점을 맞았다. 모든 음식의 스코빌 지수가 K이상인지를 확인하는 작업을
 if len([x for x in scoville if x >= K]) == len(scoville): 와 같이 비효율적으로 했기 때문이다. 스코빌지수를 담은 배열의 범위가 100만까지이기 때문에
 while문을 통해 매번 모든 원소를 확인한다면 최악의 경우 O(N^2)의 가까운 알고리즘이 되기 때문에 시간초과가 되었던 것으로 생각한다.
 이런 문제를 풀 때 heapq를 통해 우선순위큐 자료구조를 썼다고 해서 무조건 효율성이 좋아지는 게 아니라, 다른 코드에서도 효울성을 생각해야된다는 점을 깨달았다. 

'''
