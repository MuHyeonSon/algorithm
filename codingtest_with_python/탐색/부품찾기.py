# condingtest_with_python_part2_이진탐색
# 부품찾기.py

## 데이터 범위 확인해보았을 때, 1000만을 넘어가는 것은 없었음 따라서 이진탐색을 무조건 적으로 사용하지
## 않아도 되지 않나??

# 출력 : 첫 째줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no

import time

# 나의 풀이 -> 교재 확인 해보니, 이진탐색이 아닌 경우 리스트로만 탐색하는 경우는 없고, 집합 자료형 이용하는 풀이가 있음
N = int(input()) # 매장의 부품 종류 개수
market = list(map(int, input().split())) # 매장에 있는 부품 목록
M = int(input()) # 손님이 주문한 부품 종류 개수
custoumer = list(map(int, input().split())) # 손님이 주문한 부품 목록

start_time = time.time()

result = [] # 결과저장할 리스틑

for item in custoumer:
  # 주문한 제품 중 하나가 매장에 있다면
  if item in market:
    result.append("yes")
    # 그 제품을 매장 부품 목록에서 제거 (같은 제품 여러 개 찾을 경우와 같은 중복 고려하기 위해)
    market.remove(item)
  else :
    result.append("no")

for message in result:
  print(message, end = " ")

print()
end_time = time.time()
print(f'알고리즘 수행 시간 : {end_time - start_time}')

# 나의 풀이 (이진탐색 구현)

## 이진 탐색 구현(반복문)
# 나의 풀이 (이진탐색 구현)
## 이진 탐색 구현(반복문)
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else :
      start = mid + 1
  return None

## 매장의 부품 개수
n = int(input())
## 가게 있는 전체 부품 번호를 입력
market = list(map(int, input().split()))
market.sort() ################################################ ****이진 탐색을 하기 위해 정렬 수행****
## 손님이 확인 요청한 부품 개수를 입력
m = int(input())
## 손님이 확인 요청한 전체 부품 번호를 입력
customer = list(map(int, input().split()))

## 손님이 확인 요청한 부품 번호를 하나씩 확인
for component in customer:
  # 해당 부품이 존재하는지 확인
  result = binary_search(market, component, 0, n-1) 
  if result != None:
    print("yes", end = ' ')
  else :
    print("no", end= ' ')




    
# 나의 풀이 (Product Code)

# 교재 풀이 (계수 정렬)
## N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000001 # 매장의 부품 개수가 1000,000 개라고 했으므로 0포함해서 백만1

## 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] = 1

## M (손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
## 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

## 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')

# 교재 풀이 (집합 자료형 이용)

## N(가게의 부품 개수)을 입력받기
n = int(input())
## 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))
## M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
x = list(map(int, input().split()))

## 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')

# 느낀점
"""
이진탐색의 구현을 완벽히 안 보고 작성할 수 있게 되었으며,
탐색할 데이터들을 set자료형을 사용하는 것이 단순히 특정한 데이터가 존재하는지 검사할 때에
매우 효과적으로 사용할 수 있다는 것을 알게되었다.
"""
