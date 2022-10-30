# condingtest_with_python_part2_greedy
# greedy_상하좌우.py


#나의 풀이

n = int(input())
#map = [[0]*n for _ in range(n)]

x = 1
y = 1

plan = list(map(str,input().split()))

for i in range(len(plan)):
  if plan[i] == 'L':
    if 1 > (x - 1):
      continue
    else:
      x -= 1
  elif plan[i] == 'R':
    if n < (x + 1):
      continue
    else:
      x += 1
  elif plan[i] == 'U':
    if 1 > (y - 1):
      continue
    else:
      y -= 1   
  elif plan[i] == 'D':
    if n < (y + 1):
      continue
    else:
      y += 1  
  
print(y,x)


# 교재 풀이

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x,y)



# 느낀점 
"""
학습 단계2에서 코드업 문제를 풀 때 달팽이 문제와 역달팽이 문제, 등과 개미? 문제 등을
풀며 위치를 계산하는 문제를 풀었는데  그 문제에서도 조건문이 아니라 미리
정의한 방향이동을 위한 x,y에 대한 리스트를 정의했던 풀이가 기억났다. 해당 교재 풀이도 
마찬가지였으며 이 방법을 떠올리지 못했다.

또한 move_type에 대한 리스트도 따로 선언했다는 차이가 있었고 당장은
나의 풀이가 더 익숙하지만 이 방법이 시간 복잡도가 더 낮다면 이방법을 사용하는 것이 좋겠다고 생각했다.



이러한 문제는 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로
분류되며 구현이 중요한 대표적인 문제유형이다. 알고리즘 교재, 문제 풀이사이트, 등에 따라 
다르게 일컬을 수 있으니 코테에서의 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한
점이 많다는 정도로 기억하라고 한다.
그리디와 함께 구현문제는 코테에서 가장 난이도가 낮은 문제이고 논리적 사고력을 확인할 수 있는
문제이다. 그래서 합격을 좌우하는 중요한 문제이다.


"""
