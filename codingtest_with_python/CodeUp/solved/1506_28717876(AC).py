﻿"""
평소 호기심이 많은 남호는 정보고 사이트에 있는 달팽이 배열 문제를 다르게 만들고 싶었다.

입력 예시와 출력 예시를 참고 하여 n을 입력 받아 출력하는 프로그램을 작성하시오.

입력
배열의 크기 n이 입력된다. (n은 15보다 작은 홀수)

출력
역 달팽이 배열을 출력한다.

입력 예시   
5

출력 예시
1 16 15 14 13 
2 17 24 23 12 
3 18 25 22 11 
4 19 20 21 10 
5 6 7 8 9 
"""

# 역달팽이

# 상, 우, 하, 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# nr: next row, nc: next column
# cr: current row, cc: current column
r = 0 # 현재 위치의 y좌표
c = 0 # 현재 위치의 x좌표


d = 2 # 방향 전환 리스트 원소 값에 접근할 인덱스 값

n = int(input()) # 사용자로부터 2차원 배열의 크기 입력 받음
dp_list = [[0]*n for _ in range(n)] # 이차원 배열의 원소값들을 저장할 dp 리스트 생성

count = 1 # 원소의 저장할 값
while 1: 
  if count == (n*n + 1): # n*n 배열이므로 n*n 번째 숫자가 채워지면 break
    break
  else:
    dp_list[r][c] = count # 현재 위치에 count 값 저장
    r += dr[d] # 다음 위치 업데이트
    c += dc[d] # 다음 위치 업데이트
    count += 1 # 다음 원소값 업데이트

    # 방향 전환이 필요한 경우 실행 취소
    if r < 0 or r >= n  or c < 0 or c >= n or (dp_list[r][c] != 0):
      r -= dr[d] # y좌표 아동 실행 취소
      c -= dc[d] # x좌표 아동 실행 취소
      
      #방향 전환 (시계방향 (1,2,3,0 -> 우,하,좌,상))
      if d == 0:
        d = 3 # 상 -> 좌 (다시 인덱스 3으로 순환되어야 하므로)
      else:
        d -= 1
      #방향 전환 후 다음 위치 다시 업데이트
      r += dr[d] # 다음 위치 업데이트
      c += dc[d] # 다음 위치 업데이트

# 완성된 dp 테이블로부터 달팽이 2차원 배열 출력:
for i in range(n):
  for j in range(n):
    print(dp_list[i][j], end = ' ')
  print()
