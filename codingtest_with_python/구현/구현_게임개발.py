# condingtest_with_python_part2_구현
# 구현_게임개발.py 손무현

"""
맵  안에서 캐릭터가 움직이는 시스템을 개발 중

맵의 각 칸은 (A,B)
 A = 북쪽으로부터 떨어진 칸의 개수, B = 서쪽으로부터 떨어진 칸의 개수

캐릭터의 움직임에 이상이 있는지 테스트하기 위함임


# 입력 :
N,M
A,B,d
맵 (0 : 육지, 1 : 바다 (외곽 : 바다))
# 출력 : 이동을 마친 후 캐릭터가 방문한 칸의 수를 첫째 줄에 출력한다. 

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재하면 -> 왼쪽 방향으로 회전, 왼쪽으로 한 칸 전진
                                  가보지 않은 칸이 없다면 -> 왼쪽 방향으로 회전 -> 1단계로 돌아감
3. 네 방향 모두 이미 가본 칸 or 바다로 되어 있는 칸 -> (뒤쪽 방향이 바다인칸이라 뒤로 갈 수 없는 경우 움직임 멈춤)
바라보는 방향 유지한채 한 칸 뒤로 가고 1단계로 돌아감

"""


#나의 풀이

N,M = map(int,input().split()) # N : 세로 크기, M : 가로 크기
A,B,d = map(int,input().split()) # d : 방향 (0 : 북 ,1 : 동,2 : 남,3 : 서)
Map = []
count = 0
for i in range(N):
  temporary_array = list(map(int,input().split()))
  Map.append(temporary_array)


direction = [0, 3, 2, 1] # 북 서 남 동
front_direction_row = [-1, 0, 1, 0] # 북 서 남 동 (각 방향 기준으로 한칸 이동한 위치에 대한 row)
front_direction_column = [0, -1, 0, 1] # 북 서 남 동 (각 방향 기준으로 한칸 이동한 위치에 대한 column)
back_direction_row = [1, 0, -1, 0] # 북 서 남 동 (각 방향 기준으로 뒤로 한 칸 이동한 위치에 대한 row)
back_direction_column = [0, 1, 0, -1] # 북 서 남 동 (각 방향 기준으로 뒤로 한칸 이동한 위치에 대한 column)
direction_index = direction.index(d)

four_direction_check_count = 0
#Map[A][B] = 2
while (True):
  # 왼쪽 방향으로 회전
  direction_index = ((direction_index + 1) % 4) # 메뉴얼 2번 (왼쪽 방향으로 회전)
  front_row = front_direction_row[direction_index] # 왼쪽 방향으로 회전 한 후 한 칸 전진한 위치의 row
  front_column = front_direction_column[direction_index] # 왼쪽 방향으로 회전 한 후 한 칸 전진한 위치의 column

  # 메뉴얼 2번 (왼쪽 방향에 가보지 않은 칸 존재하면 왼쪽 칸으로 전진 (가본 칸을 2로 표시할 거임))
  if (0<=(A + front_row)<=N) and (0<=(B + front_column)<=M) and Map[A + front_row][B + front_column] != 1 and Map[A + front_row][B + front_column] != 2:
    Map[A + front_row][B + front_column] = 2
    A = A + front_row # 한 칸 전진
    B = B + front_column # 한 칸 전진
    count += 1 # 방문한 칸 수 1개 증가
    four_direction_check_count = 0
  else : 
    four_direction_check_count += 1
    if four_direction_check_count == 4 : # 메뉴얼 3번
      A = A - front_row # 메뉴얼 3 바라보는 방향 유지한채 한 칸 뒤로 가고 (한 칸 후진)
      B = B - front_column # 메뉴얼 3 바라보는 방향 유지한채 한 칸 뒤로 가고  (한 칸 후진)
      #A = A + back_direction_row[direction_index] # 메뉴얼 3 바라보는 방향 유지한채 한 칸 뒤로 가고 1단계로 돌아감
      #B = B + back_direction_column[direction_index]
      four_direction_check_count = 0
      if Map[A][B] == 1: # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임 멈춤
        break
  ############################## 맵 확인 코드
  print("@@@@@@@@@@@@@@@@@@@@")
  for i in range(4):
    print(Map[i])
  ##############################
  print(f' A : {A} B : {B} Map[A][B] : {Map[A][B]} direction_index : {direction_index}')

print(count)

# 나의 풀이 (Product Code)

N,M = map(int,input().split()) # N : 세로 크기, M : 가로 크기
A,B,d = map(int,input().split()) # d : 방향 (0 : 북 ,1 : 동,2 : 남,3 : 서)
Map = []
count = 0
for i in range(N):
  temporary_array = list(map(int,input().split()))
  Map.append(temporary_array)


direction = [0, 3, 2, 1] # 북 서 남 동
front_direction_row = [-1, 0, 1, 0] # 북 서 남 동 (각 방향 기준으로 한칸 이동한 위치에 대한 row)
front_direction_column = [0, -1, 0, 1] # 북 서 남 동 (각 방향 기준으로 한칸 이동한 위치에 대한 column)
direction_index = direction.index(d)

four_direction_check_count = 0

while (True):
  # 왼쪽 방향으로 회전
  direction_index = ((direction_index + 1) % 4) # 메뉴얼 2번 (왼쪽 방향으로 회전)
  front_row = front_direction_row[direction_index] # 왼쪽 방향으로 회전 한 후 한 칸 전진한 위치의 row
  front_column = front_direction_column[direction_index] # 왼쪽 방향으로 회전 한 후 한 칸 전진한 위치의 column

  # 메뉴얼 2번 (왼쪽 방향에 가보지 않은 칸 존재하면 왼쪽 칸으로 전진 (가본 칸을 2로 표시할 거임))
  if (0<=(A + front_row)<=N) and (0<=(B + front_column)<=M) and Map[A + front_row][B + front_column] != 1 and Map[A + front_row][B + front_column] != 2:
    Map[A + front_row][B + front_column] = 2
    A = A + front_row # 한 칸 전진
    B = B + front_column # 한 칸 전진
    count += 1 # 방문한 칸 수 1개 증가
    four_direction_check_count = 0
  else : 
    four_direction_check_count += 1
    if four_direction_check_count == 4 : # 메뉴얼 3번
      A = A - front_row # 메뉴얼 3 바라보는 방향 유지한채 한 칸 뒤로 가고 (한 칸 후진)
      B = B - front_column # 메뉴얼 3 바라보는 방향 유지한채 한 칸 뒤로 가고  (한 칸 후진)
      four_direction_check_count = 0
      if Map[A][B] == 1: # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임 멈춤
        break

# 교재 풀이
"""
 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적임
"""

## N,M을 공백으로 구분하여 입력받기
n,m = map(int,input().split())

## 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

## 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력 받기
x, y, direction = map(int,input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

## 전체 맵 정보 입력 받기
array = []

for i in range(n):
  array.append(list(map(int,input().split())))

## 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  #왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않는 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y = dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = [nx]
      y = [ny]
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0
## 정답출력
print(count)



# 느낀점 
"""
삼성전자 공채 코딩 테스트에서 자주 출제되는 대표적인 유형이라 하는데
문제 자체는 어렵지 않지만 구현하는데 시간이 너무 오래 걸려서
제한시간 40분안에 풀지 못하였고 이러한 문제에 익숙해져서 빨리 풀 수 있도록
계속해서 반복하는 수 밖에 없다는 생각을 하였다.
교재에서도 문제를 바르게 이해하여 소스코드로 옮기는 과정이 간단하지 않으니
반복적인 숙달이 필요하다고 말하고 있다.

구현 방법에 있어서 여러 차이점 들이 있었는데 교재 풀이의 경우
맵을 두 개를 만들어서 한 개는 주어진 맵에 대한 2차원 리스트
다른 하나는 방문한 위치를 기록하기 위한 맵에 대한 2차원리스트를
생성하였는데 나는 그냥 맵 하나를 사용하여 방문한 위치를 2라는 수로
 따로 구분하여 기록 하였다.
또한 왼쪽으로 도는 기능을 하는 함수를 따로 사용하여 코드를 간편화 하였는데
항상 계속해서 같은 기능을 사용해야되는 경우 함수로 정의하여 사용하는 것이
편리할 것이라고 생각하였고 다음에 같은 상황이 발생하면 함수를 정의하여
사용하는 것을 시도해볼 것이다. 또한 2차원 리스트를 초기화 할 때 0으로
초기화 하는 과정을 생략하였는데 이부분도 리스트 컴프리헨션을 사용하여
안전하게 초기화 해야겠다는 생각을 하였다.

전체적으로 내가 구현한 코드와 교재 풀이와 코드 작성 구조가 비슷하다고 느꼈는데
역시나 교재 코드가 훨씬 깔끔하다는 것을 알게 되었고 더 간단하게
짤 수 있는 코드를 비효율적으로 작성한 부분 들이 있었음을 알게 되었다.

네 방향에 대한 인덱스를 따로 두지 않고 북 남 동 서 순서로 -1 씩 이동하면
되었는데 이 부분을 교재풀이 대로 수정하면 더욱 간단해질 것이라고 생각했다.
"""
