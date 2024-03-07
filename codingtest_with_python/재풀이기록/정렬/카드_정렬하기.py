# 카드_정렬하기 2차 풀이

import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
    
result = 0

while len(heap) > 1:
    first_min = heapq.heappop(heap)
    second_min = heapq.heappop(heap)
    result += first_min + second_min
    heapq.heappush(heap, first_min + second_min)

print(result)



# 이전 풀이
'''
n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

num_comparision = cards.pop(0)
num_comparisions = []
#num_comparisions.append(cards.pop(-1))

cards.sort() # 최악의경우 O(NlogN)
for c in cards:
    num_comparision += c
    print(f'c : {c}')
    print(f'num_comparision : {num_comparision}')
    num_comparisions.append(num_comparision)
    print(num_comparisions)
    

print(sum(num_comparisions))
'''

# 느낀점
"""
단순히 정렬하고 가장 작은 두 수끼리 더하여 최종 비교회수를 구하면 된다고 생각하였다.
우선순위큐를 이용하여 정렬문제를 해결할 수 있고, 우선순위큐에 넣고 빼는 것만으로도 정렬이 가능함을 다시 한 번 알 수 있었다.
까먹지 않도록 지나가다가 이 문제를 마주친다면 반드시 다시 풀어봐야겠다.

heapq 라는 모듈과 이 모듈은 따로 객체를 생성하지 않고 리스트를 생성한 뒤, heapq.heappush, heapq.heappush 등을 통해 데이터를 넣고 뺄 수 있다는 것을
꼭 기억하기
"""
