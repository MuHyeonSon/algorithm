# condingtest_with_python_part2_정렬 실전문제
# 성적이낮은순서로학생출력.py (D 기업 프로그래밍 콘테스트 예선)



# 나의 풀이
N = int(input())
score_list = []
for i in range(N):
  A, B = map(str,input().split())
  score_list.append((A,int(B)))

def setting(element):
  return element[1] 


result_list = sorted(score_list,key = setting)

for student in result_list:
  print(student[0], end = ' ')

  

    
# 나의 풀이 (Product Code)

N = int(input()) # 학생 수 입력 받음
score_list = [] # 학생들의 성적 정보 저장할 리스트 선언

## 학생 정보 저장
for i in range(N):
  A, B = map(str,input().split())
  score_list.append((A,int(B)))

## 다차원 데이터에 대한 key 설정 함수(파이썬 정렬라이브러리에 사용
def setting(element):
  return element[1] # 두 번째 (index == 1) 원소를 return

## 설정한 key(성적)에 따라 학생 정보 리스트를 정렬 후 result_list에 저장
result_list = sorted(score_list,key = setting)

## 정렬된 학생 정보 한 명씩 출력(성적이 낮은 순서로)
for student in result_list:
  print(student[0], end = ' ')



    
# 교재 풀이

## N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
  input_data = input().split() ############### map안써도 바로 split 된 것들이 원소들로 이루어진 리스트로 반환됨
  # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  array.append((input_data[0], int(input_data[1])))

## key를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1]) ############## 나는 함수 따로 정의했는데 여기서는 lambda씀

# 정렬이 수행된 결과 출력
for student in array:
  print(student[0], end=' ')



# 느낀점

"""
구현하면서 sorted 파이썬 정렬라이브러리를 사용함에 있어 key 정의함수에 대해서
잠시 헷갈렸고 이를 까먹지 않도록 해야겠다고 생각했고, 또한 문제를 읽고
범위가 정해져 있고, 데이터가 100만개 이하였기 때문에 계수 정렬을
이용할 수 있지 않을까라고 생각했지만 문제에서 어떤 알고리즘을
사용하라는 요구사항이 없었으므로 파이썬 정렬 라이브러리를 사용했다.
정렬라이브러리는 최악의 경우 O(NlogN)이고, 계수정렬은 O(N)이기 때문에 계수
정렬을 사용하면 더 빠르겠지만, 데이터가 2차원 데이터였기 때문에 제한 시간을 고려하여
sorted로 구현했다. 그리고 교재풀이를 확인해보니 sorted의 인자인 key를 설정하는데
따로 함수를 구현하는 것보다 lambda를 사용하는 것이 훨씬 편하다고 느껴져서
다음부터는 lambda를 이용해야겠다고 생각했다.
"""
