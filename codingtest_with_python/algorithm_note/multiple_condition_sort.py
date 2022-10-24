# codup 3017관련
# 하나의 원소로 두 값이 들어가 있는 리스트로 이루어진 리스트를 조건에 따라 정렬 하는 함수
# ex) n = 2, a = [[1,3],[1,9]], f = 1 , s = 2
"""
  n : 원소의 개수
  a : 정렬할 리스트
  f : sorting할 첫번 째 key 인덱스
  s : sorting할 두번 째 key 인덱스
"""


def multiple_condition_sort(n,a,f,s):

  #for i in range(n):
    #a.append(list(map(int,input().split())))
  s = 0 # 리스트 원소 개수 판별 (2가 아닌지 확인하기 위한 변수)
  for i in range(n):
    if len(a[i]) != 2:
      print("원소 리스트의 개수가 2가 아닌 것이 존재합니다.")
      s = 1
      break

  if s == 0 :
    #for i in range(n):
    #  a[i].insert(0,i+1)

    a.sort(key = lambda x : (x[f],x[s]))
    #print(a)
    return(a)

n = 4
a = [[1,3], [1,9], [0,2], [9,0]]
multiple_condition_sort(2,a,1,0)


# 개선할 점 
# 1. 원소 리스트의 길이를 입력받기
# 2. 각 조건에 대해 오름차순 내림차순 조건 설정할 수 있도록 하기

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
