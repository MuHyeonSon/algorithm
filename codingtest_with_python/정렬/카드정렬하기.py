# condingtest_with_python_part3_정렬
# 카드정렬하기.py

# 나의 풀이 (교재 해설 참고)
import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) > 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    first_min = heapq.heappop(heap)
    second_min = heapq.heappop(heap)
    result += first_min + second_min
    # 카드 묶음을 합쳐서 다시 삽입
    heapq.heappush(heap, first_min + second_min)

print(result)
    



# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 분 초 )
## n개의 숫자 카드 묶음의 각각의 크기가 주어질 떄, 최소한 몇 번의 비교가 필요한지를
## 구하는 프로그램을 작성하라.

## n개의 카드 묶음
"""
n = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))

cards.sort()
compare = cards[0] + cards[1]
#compare = 0
for i in range(2, len(cards)):
    print(f'{compare} = {compare} + {compare} + {cards[i]}')
    compare = compare + compare + cards[i]

print(compare)
"""


# 교재 풀이


# 느낀점
"""
1.가장 작은 원소를 더해야한다는 점은 이해를 하였지만

2. 나의 풀이는 각 차례에 대해 가장 작은 두가지를 선택하는 것이 아니라
이전까지의 모든합을 더한 것에 나머지 중 가장 작은 값을 더한 것이었다.
그렇기 떄문에 제대로 된 답을 도출하지 못하였고,

3. 해설을 보고 우선순위큐를 이용하면 간단히 구현할 수 있다는 것과

4. 우선순위 큐에 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있음을 알게되었다.

5. 정렬에서 이렇게 우선순위큐 자료구조를 활용하여 해결할 수 있다는 문제가 있다는 것도
잘 기억해야겠다고 생각했다.
"""
