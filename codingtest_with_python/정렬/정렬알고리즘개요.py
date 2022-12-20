# condingtest_with_python_part2_
# 정렬알고리즘개요.py

## 선택정렬 소스코드 (6-1)

### 나의 풀이

array = [7,5,9,0,3,1,6,2,4,8]

for index in range(len(array)):
  print(index)
  minimum_index = index 
  if minimum_index == len(array) - 1:
    minimum_index -= 1 # 마지막 선택할 원소의 인덱스가 리스트의 전체 길이 범위를 벗어나는 것을 방지 하기 위해
  minimum_of_others_index = array.index(min(array[minimum_index + 1:]))
  if array[minimum_index] >  array[minimum_of_others_index]:
    array[minimum_index], array[minimum_of_others_index] = array[minimum_of_others_index], array[minimum_index]
  print(array)

    
### 나의 풀이 (Product Code)

array = [7,5,9,0,3,1,6,2,4,8]

for index in range(len(array)):
  minimum_index = index 
  if minimum_index == len(array) - 1:
    minimum_index -= 1 # 마지막 선택할 원소의 인덱스가 리스트의 전체 길이 범위를 벗어나는 것을 방지 하기 위해
  minimum_of_others_index = array.index(min(array[minimum_index + 1:]))
  if array[minimum_index] >  array[minimum_of_others_index]:
    array[minimum_index], array[minimum_of_others_index] = array[minimum_of_others_index], array[minimum_index]


    
### 교재 풀이

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i + 1, len(array)): ############## 내 코드와의 차이점 : 정렬되지 않은 부분 리스트에서 for 루프 사용하여 min값의 인덱스 찾음
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)


## 삽입정렬 소스코드 (6-3) ## key point, 한 칸씩 이동(스와프)!!

# 나의 풀이

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    minimum_index = -1
    if array[j-1] > array[i]:
      minimum_index = j-1
  if minimum_index != -1:    
    array.insert(minimum_index,array[i])
    array.pop(i+1)
    print(array)

print(array)
      

    
# 나의 풀이 (Product Code)


    
# 교재 풀이

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]

print(array)

## 퀵 정렬 (평균 시간복잡도 : O(N), 최악의 경우 시간 복잡도 : O(N^2))

### 동작 방식 (원소가 1개인 경우 종료)
####  파트 1 (
####    아래의 과정 반복  
####      리스트의 첫번째 데이터를 pivot으로 설정 -> 
####      왼쪽에서부터 하나씩 확인하며 pivot 보다 큰 데이터가 나오면 그것을 선택(선택한 원소는 left가 됨) ->
####      오른쪽에서부터 하나씩 확인하며 pivot보다 작은 데이터가 나오면 그것을 선택(선택한 원소는 right가 됨) ->
####      만약 엇갈리지 않았다면 left와 right의 위치를 변경 (두 데이터의 위치를 서로 변경)
####      만약 left와 rigth가 엇갈리는 상태가 되면 right(작은 데이터가 right가 되니까)와 pivot을 바꿈 
####    분할 완료
####  )
####  파트 2 (
####    (이전의 pivot과 위치를 바꾼 right를 기준으로) 양쪽으로 분할 된 왼쪽 부분 리스트에 대해 파트1과 같은 방식으로 정렬 수행 (첫번째 원소부터 right전까지)     
####  )
####  파트 3 (
####    (이전의 pivot과 위치를 바꾼 right를 기준으로) 양쪽으로 분할 된 오른쪽 부분 리스트에 대해 파트1과 같은 방식으로 정렬 수행 (right +1부터 마지막원소까지)  
####  )

### 퀵 정렬 소스코드 (6-4) ##

#### 연습 (start,end,left,right,pivot)

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] < array[pivot]:
      left += 1
    while right <= start and array[right] > array[pivot]:
      right -= 1
    if left > right:
      array[pivot], array[right] = array[right], array[pivot]
    if left < right:
      array[left], array[right] = array[left], array[right]
  
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

quick_sort(array,1,len(array)-1)


#### 교재 풀이

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]
  
  quick_sort(array,start,right - 1)
  quick_sort(array,right + 1,end)

quick_sort(array,0,len(array)-1)

print(array)

### 파이썬 장점 살린 퀵 정렬 소스코드 (6-5) ##

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:] # pivot을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

## 계수 정렬 (시간복잡도 : O(N + K),공간 복잡도 : O(N + K)) 데이터 개수 100만개 미만일 때 사용(데이터중복 多, 범위제한O, 데이터수(<100만))
### count 리스트를 만듬 (각 인덱스에는 특정 데이터의 등장횟수가 들어가 있음)
### count 리스트 자체가 정렬된 형태임 출력할 때 모든원소를 처음부터 차례대로 count의 원소값인덱스번만큼 출력하면됨
### 계수 정렬 소스코드 (6-6)

#### 연습

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = ' ')

# 파이썬의 정렬 라이브러리 (최악의 경우에도 시간 복잡도 O(NlogN)) 병합정렬 and 삽입정렬 기반

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

array = [('토마토',4),('김치',2),('샐러드',8)]

def setting(data):
  return data[1]

result = sorted(array,key = setting)  
print(result)


# 파이썬의 정렬 라이브러리 (최악의 경우에도 시간 복잡도 O(NlogN)) 병합정렬 and 삽입정렬 기반

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

array = [('토마토',6),('김치',9),('샐러드',2)]

def setting(data):
  return data[1]

result = sorted(array,key = setting)  
print(result)
