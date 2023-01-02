# condingtest_with_python_part2_이진탐색
# 반복문으로구현한이진탐색.py

# 나의 풀이

    
# 나의 풀이 (Product Code)

    
# 교재 풀이

def binary_search(array, target, start, end):
  
  while start <= end:
    mid = (start + end) // 2
    
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 더 작으면 왼쪽을 확인
    elif array[mid] > target:
      end = mid - 1
    # 중간접의 값보다 찾고자 하는 값이 더 크다면 오른쪽을 확인
    else :
      start = mid + 1
  return None

# 원소의 개수(n)와 찾고자 하는 값(target)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과를 출력
result = binary_search(array, target, 0, n -1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)

# 느낀점
