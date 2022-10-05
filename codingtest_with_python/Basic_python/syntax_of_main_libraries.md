# 표준라이브러리 중 코테를 준비하며 반드시 알아햐 하는 라이브러리 6가지

## 내장함수
print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리.

```python
# 내장함수는 별도의 import 명령어 없이 바로 사용할 수 있음


# sum()함수 -> iterable 객체가 입력으로 주어졌을 때 모든 원소의 합을 반환
result = sum([1,2,3,4,5,6,7,8,9,10])
print(result) # 출력 : 55


# min()함수 -> 파라미터 두 개 이상들어왔을 때, iteralbe 객체의 원소 중 가장 작은 값을 반환
result = min([1,2,3,4,5,6,7,8,9,10])
print(result) # 출력 : 1


# max()함수 -> 파라미터 두 개 이상들어왔을 때, iteralbe 객체의 원소 중 가장 작은 값을 반환
result = max([1,2,3,4,5,6,7,8,9,10])
print(result) # 출력 : 10


# eval()함수 -> 수학 수식이 문자열 형식으로 들어오면 그 수학 수식을 계산한 결과를 반환
result = eval("(3+5)*46")
print(result) # 출력 : 10


# sorted() -> iterable 객체가 입력으로 주어졌을 때 정렬된 결과를 반환
result = sorted([4,1,6,3]) # 오름차순으로 정렬
print(result) # 출력 : [1, 3, 4, 6]
result = sorted([4,1,6,3], reverse = True) # 내림차순으로 정렬
print(result) # 출력 : [6, 4, 3, 1]


# 특정한 기준에 따라서 정렬 수행 (정렬 기준은 key 속성을 이용해 명시)
result = sorted([('홍길동',35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result) # 출력 : [('이순신', 75), ('아무개', 50), ('홍길동', 35)]


#리스트와 같은 iterable 객체가 기본적으로 내장하고 있는 sort()함수를 사용해 정렬
data = [4,1,6,3]
data.sort() # 오름차순으로 정렬
print(data) # 출력 : [1, 3, 4, 6]

```


---
## itertools
파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리
코테에서 가장 유용하게 사용할 수 있는 클래스 -> permutations, combinations


- permutations
  : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산

- combinations
  : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산

- product
  : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산 (중복 허용)

- combinations_with_replacement
  : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산 (중복 허용)
  
```python
from itertools import permutations, combinations, product, combinations_with_replacement
data = ["A", "B", "C"]

print(list(permutations(data, 3))) # iterable 객체 'data'에서 3개를 뽑는 모든 순열 구하기
print(list(combinations(data, 2))) # iterable 객체 'data'에서 2개를 뽑는 모든 조합 구하기
print(list(product(data, repeat = 2))) # iterable 객체 'data'에서 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(list(combinations_with_replacement(data, 2))) # iterable 객체 'data'에서 2개를 뽑는 모든 조합 구하기 (중복 허용)
```
출력
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
[('A', 'B'), ('A', 'C'), ('B', 'C')]
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


---
## heapq
힙(Heap) 기능을 제공하는 라이브러리 (우선순위 큐 기능을 구현하기 위해 사용)

---
## bisect
이진 탐색(Binary Search) 기능을 제공하는 라이브러리.

---
## collections
덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리.

---
## math
필수적인 수학적 기능을 제공하는 라이브러리. (팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수, 파이(pi)와 같은 상수 포함

