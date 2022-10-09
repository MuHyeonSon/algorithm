"""
부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

입력
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

출력
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.

입력 예시   
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5

출력 예시
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
"""
h, w = map(int,input().split()) # 격자판의 세로(h), 가로(w)
n = int(input()) # 막대의 개수(n)

# girdboard = [[0]*w]*h -> 이런식으로 선언하면 얕은 복사가 일어남
gridboard = [[0 for j in range(w)] for i in range(h)] # 주의 행렬 관점으로 보지말고 그냥 가로 세로로 볼 것
for i in range(n):
    l, d, y, x = map(int,input().split()) # 길이(l), 막대를 놓는 방향(d:가로는 0, 세로는 1)(d), 좌표(y, x) -> 문제에서x,yㄹ ㅏ며  문제 오류임
    if d == 0 : # 막대가 가로방향이면
        for i in range(0,l): #가장 왼쪽위치부터 오른쪽방향으로 막대길이까지
            gridboard[y-1][x-1+i] = 1 # 1로 채움
    elif d == 1 : # 막대가 세로방향이면
        for i in range(0,l): #가장 위쪽위치부터 아래 방향으로 막대길이까지
            gridboard[y-1+i][x-1] = 1 # 1로 채움


for i in range(h):
    a, *others = gridboard[i]
    print(a,*others)
    
    
"""    
w, h = map(int,input().split()) # 격자판의 세로(h), 가로(w)
n = int(input()) # 막대의 개수(n)

# girdboard = [[0]*w]*h -> 이런식으로 선언하면 얕은 복사가 일어남
gridboard = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    l, d, y, x = map(int,input().split()) # 길이(l), 막대를 놓는 방향(d:가로는 0, 세로는 1)(d), 좌표(x, y)
    if d == 0 : # 막대가 가로방향이면
        for i in range(0,l): #가장 왼쪽위치부터 오른쪽방향으로 막대길이까지
            gridboard[y-1][x-1+i] = 1 # 1로 채움
    elif d == 1 : # 막대가 세로방향이면
        for i in range(0,l): #가장 위쪽위치부터 아래 방향으로 막대길이까지
            gridboard[y-1+i][x-1] = 1 # 1로 채움
    for i in range(h):
      a, *others = gridboard[i] #i번째 행의 원소 모두 언패킹
      print(a,*others) # i번째 행의 원소들 출력


for i in range(h):
    a, *others = gridboard[i] #i번째 행의 원소 모두 언패킹
    print(a,*others) # i번째 행의 원소들 출력
"""

