"""
학생의 번호와 수학, 정보 점수를 가진 데이터가 있다.

우리는 이를 정렬하려고 한다.

정렬 기준은 수학점수가 높은 순으로 정렬하되, 수학점수가 같으면 정보점수가 높은 순, 정보점수도 같으면 번호가 빠른 순서로 정렬하려고 한다.

입력
첫째 줄에 학생수 n(번호:1~n)가 입력된다. (1 <= n <= 1,000)

둘째 줄부터 각 줄에 수학점수, 정보점수가 입력된다. (번호는 1번 부터 ~ n번 차례대로 데이터가 입력됨)

출력
정렬된 데이터를 번호, 수학, 정보 점수 순으로 각 줄에 하나씩 출력한다.

입력 예시   
5
100 90
90 100
80 80
80 90
60 50

출력 예시
1 100 90
2 90 100
4 80 90
3 80 80
5 60 50

도움말
이 문제는 구조체를 정렬하는 문제이다.

std::sort를 이용하기 바라며 compare함수 구현 연습 문제이다.

"""

# 기억해야될 것! 
# 1. sorted() 나 sort()를 이용할 때에는 key 매개변수를 입력으로 받을 수 있음,
#   key 인자로 커스텀할 비교 함수를 넣어주면 됨.
#   비교 함수는 lambda도 가능하고 별도로 정의해도 됨.

#   오름차순 정렬 : sorted(a,key=lambda x:x[0])
#   내림차순 정렬 : sorted(a,key=lambda x:-x[0])
#   정렬기준 복수 -> 튜플로 순서대로 넣어줌
#   e.g. sorted(a, key = lambda x : (x[0],x[1]))

# 2. 내림차순으로 정렬하려면 매개변수에 reverse = True로 설정

# 오름차순 정렬 : sorted(a,key=lambda x:x[0])
# 내림차순 정렬 : sorted(a,key=lambda x:-x[0])
# 정렬기준 복수 -> 튜플로 순서대로 넣어줌
#   e.g. sorted(a, key = lambda x : (x[0],x[1]))

n = int(input())

score = [[0]*n for _ in range(n)]

score2 = []

for i in range(n):
  score2.append(list(map(int,input().split())))


for i in range(n):
  score2[i].insert(0,i+1)

score2.sort(key = lambda x : (x[1],x[2]) ,reverse = True)


for i in range(n):
  print(f'{score2[i][0]} {score2[i][1]} {score2[i][2]}')


