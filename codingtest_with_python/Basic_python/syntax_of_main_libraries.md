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
힙(Heap) 기능을 제공하는 라이브러리 (우선순위 큐 기능을 구현하기 위해 사용(다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서))

파이썬의 힙(Heap)은 최소 힙(Min Heap)으로 구성되어 있어서 단순히 힙(Heap)에 원소를 전부 넣었다가 뺴는 것만으로도 O(NlogN)에 오름차순 정렬이 완성됨.
-> 보통 최소 힙(Min Heap) 자료구조의 최상단 원소는 '가장 작은' 원소 이기 때문

- 힙(Heap)에 원소 삽입 : heapq.heqppush() 메서드 이용

- 힙(Heap)에서 원소 꺼내기 : heapq.heappop() 메서드 이용

- 오름차순 힙 정렬(Heap Sort) 구현
  ```python
  # heapq 라이브러리를 통해 힙 정렬(Heap Sort)을 구현하는 예제

  import heapq

  def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
      heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
      result.append(heapq.heappop(h))

    return result

  result = heapsort([1,3,5,7,9,2,4,6,8,0])
  print(result) # 출력 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

- 내림차순 힙 정렬(Heap Sort) 구현
  파이썬에서는 최대 힙(Max Heap)지원 X, 따라서 Max heap 구현해야할 때는 원소의 부호를 임시로 변경하는 방식 사용 
  -> 힙에 원소 삽입하기 전에 잠시 부호를 반대로 바꿈 -> 힙에서 원소를 꺼낸 뒤 부호를 바꾸면 됨
  ```python
  # heapq 라이브러리를 통해 내림차순 힙 정렬(Heap Sort)을 구현하는 예제

  import heapq

  def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
      heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
      result.append(-heapq.heappop(h))

    return result

  result = heapsort([1,3,5,7,9,2,4,6,8,0])
  print(result) # 출력 : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  ```

---
## bisect
이진 탐색(Binary Search) 기능을 제공하는 라이브러리.
-> 정렬된 배열에서 특정한 원소를 찾아야할 때 매우 효과적

*가장 중요하게 사용되는 두함수
  - bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 반환하는 메서드
  - bisect_right(a, x) :  정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 반환하는 메서드
  ```python
  from bisect import bisect_left, bisect_right
  
  a = [1,2,4,4,8]
  x = 4
  
  print(bisect_left(a,x)) # 출력 : 2  (정렬된 리스트 a에 새롭게 4를 삽입하려 할 때 가장 왼쪽 인덱스)
  print(bisect_right(a,x)) # 출력 : 4 (정렬된 리스트 a에 새롭게 4를 삽입하려 할 때 가장 오른쪽 인덱스)
  ```
  - 이 두 함수는 정렬된 리스트에서 값이 특정 범위에 속하는 원소 개수 구하고자 할 때 효과적으로 사용됨
    ```python
    from bisect import bisect_left, bisect_right
    
    # 하나의 리스트로부터 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수(left_value<=x<=right_vlaue 인 데이터의 개수를 반환하는 함수)
    def count_by_range(a, left_value, right_value):
      right_index = bisect_right(a, right_value)
      left_index = bisect_left(a, left_value)
      return right_index - left_index
    
    a = [1,2,3,3,3,3,4,4,8,9]
    
    # 값이 [4,4] 범위에 있는 데이터 개수 출력
    print(count_by_range(a,4,4)) # 출력 : 2
    # 값이 [-1,3] 범위에 있는 데이터 개수 출력
    print(count_by_range(a,-1,3)) # 출력 : 6
      
    ```
---
## collections
덱(deque), 카운터(Counter) 등의 코테에서 유용한 자료구조를 포함하고 있는 라이브러리.

- 덱(deque)
  
  - 파이썬에서는 deque를 사용해 que를 구현해야한다. 
    -> 원소 삽입은 append로, 원소 삭제는 popleft()로 사용하면 됨 (선입선출)
  
  - 가장 앞쪽에 원소 추가, 가장 앞쪽에 있는 원소 제거를 수행할 때의 시간복잡도는 리스트는 O(N) deque는 O(1)
  
  - deque는 인덱싱 슬라이싱 등의 기능 사용할 수 없음

  - deque는 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입or 삭제할 때 매우 효과적
  
  - deque는 스택, 큐의 기능을 모두 포함한다고 볼 수 있음 -> 스택 혹은 큐 자료구조 대용으로 사용 가능
  
  - 첫 번째 원소 제거 : popleft() 사용
  
  - 마지막 원소 제거 : pop()

  - 첫 번째 인덱스에 원소 x삽입 : appendleft(x)
  
  - 마지막 인덱스에 원소 삽입 append(x)
  
  ```python
  from collections import deque
  
  data = deque([2,3,4,5,6,7])
  data.appendleft(1) # 리스트의 가장 앞쪽에 원소 1 삽입
  data.append(8) # 리스트의 가장 뒤쪽에 원소 8 삽입
  
  print(data) # 출력 : deque([1, 2, 3, 4, 5, 6, 7, 8])
  # deque를 리스트 자료형으로 변환
  print(list(data)) # 출력 : [1, 2, 3, 4, 5, 6, 7, 8] 
  ```
  

- 카운터(Counter)
  
  리스트와 같은 iterable 객체가 주어졌을 때 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌
  
  ```python
  from collections import Counter
  
  c = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
  
  
  print(c) # 출력 : Counter({'blue': 3, 'red': 2, 'green': 1})
  
  print(dict(c)) # 출력 : {'red': 2, 'blue': 3, 'green': 1}
  
  print(c['blue']) # 출력 : 3
  
  print(c['green']) # 출력 : 1

  ```
  
---
## math
필수적인 수학적 기능을 제공하는 라이브러리. (팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수, 파이(pi)와 같은 상수 포함

```python
import math

# factorial(x) -> x!를 계산
print(math.factorial(5)) # 출력 : 120

# sqrt(x) -> x의 제곱근 반환 
print(math.sqrt(7)) # 출력 : 2.6457513110645907

# gcd(a,b) -> a와 b의 최대 공약수를 반환 
print(math.gcd(21,14)) # 출력 : 7

# (파이)pi, (자연상수)e 
print(math.pi) # 출력 : 3.141592653589793
print(math.e) # 출력 : 2.718281828459045

```

# 자신만의 알고리즘 노트 만들기

모르는 문제나 어려운 문제 만나면 -> 문제를 복습하며 소스코드를 정리 할 것
  
  -> 본인만의 라이브러리 노트에 기록해서 해당 문제를 해결하기 위해 사용한 기능을 라이브러리화 할 것.
     단순히 함수만 작성X, 해당 함수의 사용 예시까지 기록할 것.
