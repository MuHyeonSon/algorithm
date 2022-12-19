# condingtest_with_python_part2_DFS&BFS
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
