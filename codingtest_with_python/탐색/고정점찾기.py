# condingtest_with_python_part3_이진탐색
# 고정점찾기.py

# 나의 풀이 (교재 해설 참고)

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
            #if array[mid] == mid:
            #    return True
        elif array[mid] > mid:
            end = mid - 1
        elif array[mid] < mid:
            start = mid + 1
    return None

#n = int(input())
#data = list(map(int, input().split()))

data = list(range(100000))
for i in range(len(data)):
    data[i] -= 1
data[-1] += 1
n = len(data)

result = binary_search(data, 0, n - 1)
if result == None:
    print(-1)
else:
    print(result)

# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 분 초 )
## 고정점을 출력하는 프로그램을 작성하라
## 고정점은 한 개만 존재
## 고정점 : 값이 인덱스와 동일한 원소
## 근데 결국 모든 원소를 다 확인해 봐야되는 거 아님? 그럼 O(N)이 잖아
## O(logN)으로 설계해야하므로 이진탐색을 써야됨은 확실하다.
## 과연 이진탐색을 어떻게 사용해야 고정점을 찾을 수 있는가

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
            #if array[mid] == mid:
            #    return True
        elif array[mid] > mid:
            end = mid - 1
        elif array[mid] < mid:
            start = mid + 1
    return None

n = int(input())
#data = list(map(int, input().split()))
"""
data = list(range(100000))
for i in range(len(data)):
    data[i] -= 1
data[-1] += 1
n = len(data)
"""

result = binary_search(data, 0, len(data) - 1)
if result == None:
    print(-1)
else:
    print(result)

#for d in data:
#    temp = binary_search(data, d, 0, len(data) - 1)
#    if 0 <= temp < len(data) and data[temp] == temp:
#        print(temp)
#        break

# 교재 풀이
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)
    
n = int(input())
array = list(map(int, input().split()))

# 이진 탐색(Binary Search) tngod
index = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
else:
    print(index)
    

# 느낀점
"""
'찾고자 하는 값(target)'이 '중간점'과 동일하다고 가정하고, 탐색을 수행하면 된다는 것이
계속 이해가 가지 않아 직접 과정을 적어보니 이해가 되었다. 데이터가 정렬된 상태로 주어지기 때문에
중간점과 중간점이 가리키는 위치의 값과 크기 비교를 통해 이진탐색과 마찬가지로 중간점을 기준으로
왼쪽 부분과 오른쪽 부분을 확인하는 것이 가능하다는 것을 알게되었다.
"""
