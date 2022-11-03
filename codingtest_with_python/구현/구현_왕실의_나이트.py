# condingtest_with_python_part2_greedy
# 구현_왕실의_나이트.py
# 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성
# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있음.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기


#나의 풀이

## 위치를 구하는 경우
column = [0,'a','b','c','d','e','f','g','h'] # 수평에 대한 위치 정보를 숫자로 변환하기 위한 리스트

move_row = [1,2,-1,-2,1,2,-1,-2] # 움직일 수 있는 위치 (행)
move_column = [2,1,2,1,-1,-2,-1,-2] # 움직일 수 있는 위치 (열)

location = input() # 입력받음
location_row = int(location[1]) # 행
location_column = int(column.index(location[0])) # 열

count = 0

for i in range(8): 
  if (0 < (location_column + move_column[i]) <= 8) and (0 < (location_row + move_row[i]) <= 8):
    #print(column[location_column + move_column[i]] + str(location_row + move_row[i]))
    count += 1

# 결과 출력
print(count)


# 교재 풀이

## 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

## 나이트가 이동할 수 있는 8가지 방향 정의

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

## 8가지 방향에 대해 각 위치로 이동이 가능한지 확인

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)

# 느낀점 
"""
교재에 풀이가 더 이해하기에 쉽고 리스트를 사용하지 않고 ord를 사용해 변환하는 방법이 있었다는 것을
알 수 있었다.

"""


#print((0 < (location_row + move_row[0]) <= 8) and (0 < (location_column + move_column[0]) <= 8))
#print((0 < (location_row + move_row[1]) <= 8) and (0 < (location_column + move_column[1]) <= 8))
#print(((location_row + move_row[0])))
#print(((location_column + move_column[0])))
#print(((location_row + move_row[1])))
#print(((location_column + move_column[1])))



#print(location)
#print(location_row)
#print(location_column)


# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있음.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

"""
#나의 풀이

## 위치를 구하는 경우
column = [0,'a','b','c','d','e','f','g','h']

move_row = [1,2,-1,-2,1,2,-1,-2]
move_column = [2,1,2,1,-1,-2,-1,-2]

location = input()
location_row = int(location[1])
location_column = int(column.index(location[0]))
location_after_move1 = [0,0]

for i in range(8): 
  if (0 < (location_column + move_column[i]) <= 8) and (0 < (location_row + move_row[i]) <= 8):
    print(column[location_column + move_column[i]] + str(location_row + move_row[i]))

"""
