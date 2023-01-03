# condingtest_with_python_part2_이진탐색
# 떡볶이떡만들기.py

# 나의 풀이
N, M = map(int,input().split()) # N: 떡의 개수, 요청한 떡의 길이 : M
H = list(map(int, input().split()))
maximum_of_height = 0

## 생각 1 : 최대값에서 M만큼 뺀 값을 전체 리스트에 모든 원소에 대해 계산해보고 그 리스트의 전체 합을 구한다.
## -> 전체합이 M보다 크거나 같을 때까지 M을 1씩 증가시키면서 같은 과정을 반복한다. 마지막에 결정되는 숫자가 최대값이다.
## 생각 2 : 범위 확인했을 때 떡의 범위가 1부터 2억이므로 이진탐색쓰자 
## 리스트내의 최대값의 개수를 구하고 높이의 최대값을 최대값 - 1로 설정했을 때 최대값 개수 * 1 이 M보다 크거나 같다면 그 값을 return
## 만약 -
## 생각 3 : 최대값과 그다음으로 큰 값의 차를 이용, 그 차가 M보다 크다면 최대값 - M을 반환
##          만약 M보다 크지 않다면 2번째로 큰 값과 3번째로 큰값의 차를 구하고 

H.sort() # 이진탐색 쓰기 위한 기본 조건을 맞추기 위해 정렬 수행

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = m - 1
    else :
      start = m + 1
  return None



# 나의 풀이 (교재 해설)

## 떡의 개수(N)와 요청한 떡의 길이(M) 입력 받기
N, M = map(int, input().split())
##  각 떡의 개별 높이 입력받기
array = list(map(int, input().split()))

## 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array) # 절단기 높이 안에 있어야 떡이 잘릴 수 있으므로

result = 0 # 결과 값 저장할 변수

## 이진 탐색 수행
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      # 잘랐을 때의 떡의 양 계산하여 총 합에 더함
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total < M:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid ########### 최대한 덜 잘랐을 때가 정답이기 때문에, 우선 여기에서 result에 기록
    start = mid + 1

# 정답 출력
print(result)
  

    
# 교재 풀이


# 느낀점


# 나의 풀이 (Product Code)

    
# 교재 풀이


# 느낀점
"""
해당 문제를 실전에서 만났다면 이진탐색 문제라는 것을 알지 못했을 것 같다.
몇 가지 접근 법을 생각해보았지만 숫자가 커지면 너무 비효율적일 것이라는 생각이들었다.
하지만 데이터의 범위의 크기가 10억이었기 때문에 보고 이진탐색을 써야 되지 않을까하는 생각은 하였다.
교재에서 처리해야할 데이터의 개수가 값이 1000만 단위 이상으로 넘어가면 이진탐색과 같이 O(logN)의 솟도를 내야하는 경우가
많다고 했기 때문이다.
해설을 보고나서 풀 수 있었고, 이진탐색을 이런식으로 응용할 수 있다는 것을 알게 되었고,
이진탐색 문제이자 파라메트릭 서치 유형의 문제라는 것도 알게 되었다.
또한 이진탐색임에도 별도의 정렬 과정을 수행하지 않을 수 있다는 점이 인상 깊었다.
"""
