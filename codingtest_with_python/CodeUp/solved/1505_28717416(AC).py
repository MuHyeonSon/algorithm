"""
n이 입력되면 크기가 n인 다음과 같은 2차원 배열을 출력하시오.

입력 예)
3
출력 예)
1 2 3
8 9 4
7 6 5
입력
2차원 배열의 크기 n이 입력된다.(n<=50)

출력
크기가 n인 달팽이 배열을 출력한다.(설명참조)

입력 예시   
2

출력 예시
1 2 
4 3 
"""
## 도무지 모르겠어서 reference 참고
# 인덱스를 활용해서 방향전환을 하고 싶을 대 'delta row'와 'delta column'리스트를 만들고
# 접근하면 됨!

# 상, 우, 하, 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# nr: next row, nc: next column
# cr: current row, cc: current column
cr = 0 # 현재 위치의 y좌표
cc = 0 # 현재 위치의 x좌표
nr = 0 # 다음 위치의 y좌표
nc = 0 # 다음 위치의 x좌표

d = 1 # 방향 전환 리스트 원소 값에 접근할 인덱스 값

n = int(input()) # 사용자로부터 2차원 배열의 크기 입력 받음
dp_list = [[0]*n for _ in range(n)] # 이차원 배열의 원소값들을 저장할 dp 리스트 생성

count = 1 # 원소의 저장할 값
while 1:
  #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
  #print(f'cr : {cr}, cc : {cc}')
  #print(f'nr : {cr}, nc : {cc}')
  #print(f'd : {d}')
  #print(f"condition : {(dp_list[cr][cc] != 0) or ((cr == 0 and cc == n-1) or (cr == n-1 and cc == n-1) or (cc == 0 and cr == n-1))}") 
  #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@') 

  if count == (n*n + 1): # n*n 배열이므로 n*n 번째 숫자가 채워지면 break
    break
  else:
    dp_list[cr][cc] = count # 현재 위치에 count 값 저장

    # 다음 위치 계산
    ## 처음 위치를 제외한 꼭지점 위치일 때 방향 전환해야 됨
    if ((cr == 0 and cc == n-1) or (cr == n-1 and cc == n-1) or (cc == 0 and cr == n-1)):
      #print(f"condition : {(dp_list[cr][cc] != 0) or ((cr == 0 and cc == n-1) or (cr == n-1 and cc == n-1) or (cc == 0 and cr == n-1))}") 
      #print('방향전환O')
      if d == 3: #방향 전환 (시계방향 (1,2,3,0 -> 우,하,좌,상))
        d = 0 # 좌 -> 상 (다시 0인덱스로 순환되어야 하므로)
      else:
        d += 1
      nr = cr + dr[d] 
      nc = cc + dc[d]
      count += 1
      cr = nr
      cc = nc
    ## 꼭지점 위치의 값은 아닌 경우
    else:
      ### 그 다음 위치가 0이 아닌경우 (이미 지나친 경우) -> 방향전환해야됨
      tr = cr + dr[d] # 원래 진행방향으로 진행할 경우 다음 위치의 y좌표 (그대로 진행할 경우 그 위치가 이미지나친 경우인지를 판별하기 위해)
      tc = cc + dc[d] # 원래 진행방향으로 진행할 경우 다음 위치의 x좌표 (그대로 진행할 경우 그 위치가 이미지나친 경우인지를 판별하기 위해)
      if dp_list[tr][tc] != 0 :
        #print(f"condition : {(dp_list[cr][cc] != 0) or ((cr == 0 and cc == n-1) or (cr == n-1 and cc == n-1) or (cc == 0 and cr == n-1))}") 
        #print('방향전환O')
        d = (d + 1) % 4 # (우 -> 하 -> 좌 -> 상 1->2->3->0)시계방향으로 순환하도록 4로 나눠줌
        nr = cr + dr[d] 
        nc = cc + dc[d]
        count += 1
        cr = nr
        cc = nc

      ### 방향을 전환해야되는 경우가 아닌 경우들
      else : # 이전에 갔던 방향과 동일한 방향으로 그대로 이동
        #print('방향전환X')
        #print(f"condition : {(dp_list[cr][cc] != 0) or ((cr == 0 and cc == n-1) or (cr == n-1 and cc == n-1) or (cc == 0 and cr == n-1))}") 
        
        nr = cr + dr[d] 
        nc = cc + dc[d]
        count += 1
        cr = nr
        cc = nc

# 완성된 dp 테이블로부터 달팽이 2차원 배열 출력:
for i in range(n):
  for j in range(n):
    print(dp_list[i][j], end = ' ')
  print()


# 이것보다 훨씬 간단하게 짤 수 있다!!!!!!!!!!!!
# 코드가 길어진 이유가 다음 이동 위치가 0인지 아닌지를 판별하기 위해
# 다음 위치가 인덱스가 범위를 초과하는 인덱스인지와 따로 구별하였는데
# 그렇게 하지 않고 하나의 조건문에서 다 판별할 수 있고
# 그렇게 하기 위해서는 일단 다음 인덱스가 0이 아닌경우를 다시 빼주면 됨 (실행 취소)
# nr nc cr cc tr tc 가 아닌 그냥 c r 2가지 만으로도 짧게 구현 가능

