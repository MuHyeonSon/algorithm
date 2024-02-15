# 왕실의 나이트
# 8x8 좌표 평면
# 특정한 한 칸에 나이트 서있음
# 이동 할 때는 L자 형태로만 이동 가능
## 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
## 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 정원 밖으로 못나감
# 
# 8x8좌표 평면상에서 나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하라
# 행의 위치는 1~8
# 열의 위츠는 a~h
# a1 => 2

# 제한시간 : 20분, 풀이시간 : 16

column = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#print(column.index('a'))
bang_hyang = [(2, 1), (-2,1), (-2, 1), (-2, -1), (1, 2), (-1,2), (-1, 2), (-1, -2)] # 행, 열

result = 0
position = input()
row = int(position[1])
col = int(column.index(position[0]))

for bh in bang_hyang:
    temp_row = row + bh[0]
    temp_col = col + bh[1]
    if 1<= temp_row <= 8 and 1<= temp_col <= 8:
        result += 1

print(result)
    

'''
생각해볼점

'''
