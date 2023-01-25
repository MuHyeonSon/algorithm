# condingtest_with_python_part3_정렬
# 국영수.py

# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 분 초 )
# 범위가 크지 않으므로 파이썬 정렬라이브러리 이용

n = int(input())
data = []
for _ in range(n):
    name, korean, english, math = map(str, input().split())
    data.append((name, int(korean), int(english), int(math)))

data.sort(key = lambda x : x[0])
data.sort(reverse = True, key = lambda x :  x[3])
data.sort(key = lambda x : x[2])
data.sort(reverse = True, key = lambda x : x[1])

for d in data:
    print(d[0])


# 교재 풀이
n = int(input())
students = [] # 학생 정보를 담을 리스트

## 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())
    
'''
    1 두 번쨰 원소를 기준으로 내림차순 정렬
    2 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
    3 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
    4 네 번째 원소가 같은 경우, 첫 번재 원소를 기준으로 내림차순 정렬
'''

students.sort(key = lambda x : (-int(x[1], int(x[2]), -int(x[3]), x[0]))
  
## 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])            


# 느낀점
"""
해당 문제를 풀어보고나서 처음 알게 된 것들과 꼭 짚고 넘어가야 될 부분들은 다음과 같다.

1. 파이썬에서 튜플을 원소로 하는 리스트가 있을 때, 그 리스트를 정렬하면 기본적으로
각 튜플을 구성하는 원소의 순서에 맞게 정렬됨.
ex, 모든 원소가 첫 번째 순서에 맞게 정렬되고, 첫번째 원소 값이 같은 경우 두 번째 원소의
순서에 맞게 정렬, 두 번째 원소의 값까지 같은 경우 세 번쨰 원소의 순서에 맞게 정렬...
이런식으로 됨.

2. 또한 리스트의 원소를 정렬할 때, sort()함수의 key 속성에 값을 대입하여
원하는 '조건'에 맞게 튜플을 정렬시킬 수 있음.
ex) 첫번째원소는 오름차순., 두번째원소에 대해서는 내림차순, 이런식으로

해당 문제에서 그것을 사용하면 다음과 같다.

students.sort(key = lambda x : (-int(x[1], int(x[2]), -int(x[3]), x[0]))
    1 두 번쨰 원소를 기준으로 내림차순 정렬
    2 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
    3 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
    4 네 번째 원소가 같은 경우, 첫 번재 원소를 기준으로 내림차순 정렬
    
실전에서 해당 유형 문제를 만나면 실수없이 최대한 빠르게 풀 것이다.
"""
