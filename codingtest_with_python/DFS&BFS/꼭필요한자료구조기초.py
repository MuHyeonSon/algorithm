# condingtest_with_python_part2_DFS/BFS
# 꼭필요한자료구조기초.py

## 5-1.py 스택 예제
print("5-1.py 스택 예제")
stack = []

### 삽입(3) - 삽입(2) - 삽입(7) - 삭제() - 삽입(6) - 삽입(5)

stack.append(3)
stack.append(2)
stack.append(7)
stack.pop()
stack.append(6)
stack.append(5)

print("5-1.py 스택 예제")
print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력


## 5-2.py 큐 예제
print("5-2.py 큐 예제")

from collections import deque

queue = deque()

### 삽입(3) - 삽입(2) - 삽입(7) - 삭제() - 삽입(6) - 삽입(5)

queue.append(3)
queue.append(2) 
queue.append(7)
queue.popleft()
queue.append(6)
queue.append(5) 

print(queue) # 들어온 순서 대로 출력
queue.reverse() # 역순으로 바꿈
print(queue) # 나중에 들어온 원소부터 출력

## deque 객체를 리스트 자료형으로 변경
list(queue)

## 5-3.py 재귀 함수 예제
### DFS와 BFS를 구하려면 재귀 함수도 이해하고 있어야 함 (재귀함수 : 자기 자신을 다시 호출하는 함수)
def recursive_function():
  print("재귀 함수를 호출합니다.")
  recursive_function()

recursive_function()

## 5-4.py 재귀 함수 종료 예제
def recursive_function_exit(i):
  if i == 100 :
    return
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출한다.')
  recursive_function_exit(i + 1)
  print(i, '번째 재귀 함수를 종료합니다.')


recursive_function_exit(1)

## 5-5.py 2가지 방식으로 구현한 펙토리얼 예제

### 반복적으로 구현한 n!
def factorial_iterative(n):
  number = 1
  for i in range(n,0,-1):
    number *= i
  return number

### 재귀적으로 구현한 n!
def factorial_recursive(n):
  if n == 1:
    return 1
  else:
    return factorial_recursive(n-1) * n

print(f'반복적으로 구현한 팩토리얼 결과 : {factorial_iterative(5)}')
print(f'재귀적으로 구현한 팩토리얼 결과 : {factorial_recursive(5)}')

# 재귀 함수가 반복문을 이용하는 것과 비교햇을 때 더욱 간결한 형태임 하지만 코드를
# 딱 봤을 때 직관적이지 않기 때문에 무엇을 하는 코드인지 바로 이해하기 힘듬
