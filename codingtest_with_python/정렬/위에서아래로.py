# condingtest_with_python_part2_정렬
# 위에서아래로.py
## 문제 : 하나의 수열에는 다양한 수가 존재함, 이러한 수는 크기에 상관없이 나열되어 있음, 이 수를 큰 수부터 작은 수의 순서로 정렬해야됨,
##        수열을 내림차순으로 정렬하는 프로그램을 만들어라.
## 입력 조건 : 첫째 줄에는 수열에 속해있는 수의 개수 N(1<=N<=500)이 주어짐, 둘째 줄부터 N + 1번째 줄까지 N개의 수(1<=x<=100,000)가 입력됨,
## 출력 조건 : 입력으로 주어진 수열이 내림차순으로 결과를 공백으로 구분하여 출력, (동일한 수의 순서는 자유롭게 출력해도 괜찮)  


# 나의 풀이
N = int(input())
array_of_sequence = []
for i in range(N):
  array_of_sequence.append(int(input()))

array_of_sequence.sort(reverse = True)
for element in array_of_sequence:
  print(element, end = ' ')

    
# 나의 풀이 (Product Code)
N = int(input()) # 수열의 수 입력받기
array_of_sequence = [] # 수열의 수들을 저장할 리스트 선언
for i in range(N):
  # 수열의 수들을 저장할 리스트에 입력받은 수들을 삽입
  array_of_sequence.append(int(input()))

array_of_sequence.sort(reverse = True) # 파이썬 정렬 라이브러리를 이용하여 수열의 수들에 대한 리스트를 내림차순으로 정렬
for element in array_of_sequence:
  # 요구사항에 맞추어 수열의 수를 하나씩 출력
  print(element, end = ' ')

    
# 교재 풀이

## N을 입력받기
n = int(input())

## N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True) ########## 교재에서는 sort가 아닌 sorted 사용했음

#ㅈ 정렬이 수행된 결과를 출력
for i in array:
  print(i, end=' ') 





# 느낀점
"""
해당 문제가 기본적인 정렬을 할 수 있는 문제라는 것을 알게되어 그러한 문제는 이런식으로 
출제될 수 있다는 것을 알게 되었고, 또한 해설을 통해 수의 개수의 범위와 수의 범위(데이터의 개수)를
우선 확인해야된다는 것을 다시 한 번 알게 되었고, 이 문제와 같이 모든 범위가 크지 않은 경우
앞서 다루었던 선택 정렬, 삽입 정렬, 퀵정렬, 계수정렬 중 아무거나 이용해도 상관 없다는 것을
알게됐고, 특별한 조건이 주어져 있지 않으므로 파이썬 정렬라이브러리를 이용하는 것이 좋다는 것도
직접 풀어보며 알게되었다. 
"""
