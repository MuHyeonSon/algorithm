# condingtest_with_python_part3_이진탐색
# 공유기설치.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 50분, 풀이 시간 : 분 초 )
## c개의 공유기를 설치하려고 할 때 가장 인접한 두 공유기 사이의 거리를 크게하여 설치하려고 함
## 가장 인전합 공유기 사잉의 최대 거리를 출력하라
## 각 숫자는 집의 좌표임
## 1, 4, 8의 경우 가장인접한 두 공유기 사이의 거리가 3이고, 이보다 더 크게 만들 수 없음
## 데이터의 크기가 10억 단위이므로 이진탐색을 사용해야 될 터인데,
## 어떻게 하지??
## 1. 우선 집 좌표들을 데이터를 정렬하고,
## 2. 집 좌표 들 중 2개의 좌표를 찾아 그것에 거리를 구함
"""
def binary_search(array, c, start, end):
    result = []
    o_start = start
    o_end = end
    o_mid = (start + end) // 2
    for _ in range(c - 2):
        mid = (start + end) // 2
        result.append(array[mid])
        end = mid - 1
    
    start = o_mid + 1
    end = o_end
    for _ in range(c - 2):
        mid = (start + end) // 2
        result.append(array[mid])
        start = mid + 1
    
    result.insert(0, array[0])
    result.append(array[-1])    
    
    min_value = 0
    for i in range(1, len(result)):
        min_value = max(min_value, result[i] - result[i - 1])
    return min_value
            
        
         
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort() # 내림차순으로 정렬

print(binary_search(data, c, 0, n - 1))
"""
# 교재 풀이

## 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = map(int, input().split())

## 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 가장 인접한 두 공유기 사이의 거리의 최소 거리(가능한 최소 거리(min gap))
end = array[-1] - array[0] # 가장 인접한 두 공유기 사이의 거리의 최대 거리(가능한 최대 거리(max gap))
result = 0

## 이진탐색 수행
while (start <= end):
    mid = (start + end) // 2 # 가장 인접한 두 공유기 사이의 거리(gap)
    value = array[0] # 첫 번쨰 위치에는 기본적으로 설치
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1   
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우 거리를 증가(최솟값을 증가시킴)
        start += 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소(최댓값을 감소시킴)
        end -= 1

print(result)

# 느낀점
"""
1.해결방법을 제대로 구현시키지 못했고,
2. 교재해설읽어도 이해가 너무 안돼서 검색해보았고,
3. 코드를 같이 보았더니 겨우 이해가 되었다.
4. 가래떡 문제와 같이 이러한 파라메트릭 서치 유형의 문제는 정말 어려운 것 같다고 느꼈는데
5. 항상 이진탐색을 이용해서 하나의 지점을 찾는 다는 것을 느꼈고
6. 이 문제에서는 그것이 가장 인접한 두 공유기 사이의 거리였던 것이다.
7. 그러기 위해서는 가장 인접한 두 공유기 사이의 거리를 찾는 과정을 이진탐색을 이용하며,
그것에 필요한 범위와 조건들을 설정하는 것에 익숙해져야 겠다고 생각했다.
"""
