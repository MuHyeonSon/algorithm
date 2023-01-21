# condingtest_with_python_part3_구현
# 치킨배달.py



# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 40분, 풀이 시간 : 분 초)
import itertools

## n : 도시 한 변의 크기 , m : 남길 치킨 집의 개수
## 문제에서 주어지는 인덱스는 1,1부터 시작임!!!
n, m = map(int, input().split())

## 도시의 정보 입력받기
## 0 : 빈칸, 1 : 집, 2 : 치킨집
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

## 집과 치킨집 각각의 위치정보들을 리스트에 저장
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i+1, j+1))
        elif graph[i][j] == 2:
            chickens.append((i+1, j+1))

city_distance = 999999999 # 도시거리 초기화
for i in range(1, m + 1):
    # 치킨집들 중 i 개를 뽑아서
    temp = list(itertools.combinations(chickens, m))
    # i개들을 뽑는 모든 경우들에서 한 개를 꺼내서
    for case in temp:
        chicken_distances = [] # 치킨 거리 리스트
        # 치킨 거리를 구하기
        for h in houses:
            chicken_distance = 999999999
            for c in case:
                chicken_distance = min(chicken_distance, abs(h[0] - c[0]) + abs(h[1] - c[1]))
            chicken_distances.append(chicken_distance)
        # 도시의 치킨거리 구해서 더 작으면 그 값으로 업데이트(도시의 치킨 거리는 모든 집의 치킨 거리의 합)
        city_distance = min(city_distance, sum(chicken_distances))
## 결과 출력
print(city_distance)       

# 교재 풀이
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2: 
            chicken.append((r, c)) # 치킨집

## 모든 치킨 집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

## 치킨거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

## 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)


# 느낀점
"""
다 구했다고 생각했지만 한 부분이 꼬여서 제대로 답을 내지 못했다.

1. 내가 실수한 부분은 "치킨집들을 모두 남긴 상태에서 치킨거리를 구하고 그 치킨 거리들 중 몇 개를 뽑는 방식으로 코드를 작성한 것"이다.
치킨 집 몇개를 남기는 지, 그리고 어떤 치킨 집을 남길지 선택을 한 후에 치킨거리들을 구했어야 했었던 것이었다. 
^^^^^^^^^^^^^^^^^^^^^^
||||||||||||||||||||||

실수한 부분에 대해서 아이디어가 잘못되었었다는 것을 인지하지 못했다.
치킨 집들 중 일부가 사라지면 당연히 모든 집들에 대한 치킨거리도 바뀔 수 있다는 것을 너무 뒤늦게 알아차린 것이었다.

2. 허나 교재에서는 1부터 m개를 뽑는 경우를 모두 고려한 것이 아니라 m개의 치킨집을 뽑는 경우만 계산했다.
위에서 언급한 "치킨집 몇개를 남기는지" 자체를 고려하지 않았다....

3. 또한 itertools.combinations 를 그냥 combinations로 사용해도 됐음을 알게됐다.
"""
