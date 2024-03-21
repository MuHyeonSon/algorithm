# condingtest_with_python_part3_이진탐색
# 정렬된_배열에서_특정_수의_개수_구하기.py

# 나의 풀이
from bisect import bisect_left, bisect_right 

def count_by_range(data, target):
    left = bisect_left(data, target)
    right = bisect_right(data, target)
    return right - left

n, x = map(int, input().split())
data = list(map(int, input().split()))
result = count_by_range(data, x)
if result >= 0:
    print(-1)
else:
    print(result)

""" 생각할점 or 느낀점
bisect_left, bisect_right의 동작과 이것을 이용하여 정렬되어 있는 데이터에서 특정 값의 개수를 효과적으로 구할 수 있음을
다시 한 번 짚고 넘어갈 수 있었다.
"""
