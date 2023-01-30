# condingtest_with_python_part3_이진탐색
# 고정점찾기.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 분 초 )
## 고정점을 출력하는 프로그램을 작성하라
## 고정점은 한 개만 존재
## 고정점 : 값이 인덱스와 동일한 원소
## 근데 결국 모든 원소를 다 확인해 봐야되는 거 아님? 그럼 O(N)이 잖아
## O(logN)으로 설계해야하므로 이진탐색을 써야됨은 확실하다.
## 과연 이진탐색을 어떻게 사용해야 고정점을 찾을 수 있는가

n = int(input())
data = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
            #if array[mid] == mid:
            #    return True
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return False
for d in data:
    temp = binary_search(data, d, 0, len(data) - 1)
    if 0 <= temp < len(data) and data[temp] == temp:
        print(temp)
        break

# 교재 풀이

# 느낀점
"""
"""

"""
📰 Codingtest_with_python_part3_이진탐색_고정점찾기
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 이진탐색 문제 풀이 느낀점
"""
