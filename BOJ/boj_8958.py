"""

#BOJ8958 손무현

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

출력
각 테스트 케이스마다 점수를 출력한다.

예제 입력 1 
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
예제 출력 1 
10
9
7
55
30

"""

n = int(input()) # 숫자 n
total_score = 0 # 결과 한 개에 대한 총합 점수
for i in range(n):
  score = 0 # 최종 점수를 계산하기 위해 list_result에 하나의 원소를 계산하기 위한 변수
  result = input() # 사용자로부터 입력 받을 결과 
  n_result = len(result) # 입력 받은 결과의 문제 수
  list_result = [0]*n_result # 결과 한 개에 대한 점수들을 저장할 리스트
  for i in range(n_result): # 하나의 결과에 대해 1번 문제 부터 하나씩 불러와서
    if result[i] == 'O': # i번 문제가 맞았다면
      score += 1 # 임시 score에 1 더함
      list_result[i] = score # 해당 문제 번호에 대한 점수를 입력
    elif result[i] == 'X': # i번 문제가 틀렸다면
      score = 0 # 임시 score 0으로 초기화
      list_result[i] = 0 # 해당 문제 번호에 대한 점수 입력
  total_score = sum(list_result) # 해당 결과에 대한 총합을 계산하여 변수에 저장
  print(total_score) # 해당 결과에 대한 총합 점수 출력
