from class_Stack import*

# 해당위치가 갈 수 있는 위치인지를 체크하는 함수
def isValidPos(x,y):
    if x<0 or y<0 or x>= MAX_SIZE or y>= MAX_SIZE :
        return False
    else:
        return map[x][y]=='0' or map[x][y]=='x' # 0 : 갈 수 있는 길, x : 출구, 1 : 막힌길, . : 지나온 길
    
# 길이우선탐색(미로 탐색) : 스택 사용
def DFS():
    stack = Stack()
    stack.push((1,0)) #시작위치 (1,0)
    print('DFS:')
    
    while not stack.isEmpty():
        here = stack.pop()
        print(here,end='->')
        (x,y) = here
        if map[x][y] == 'x':  #출구이면 종료
            return True
        else:
            map[x][y]=''    #현재위치를 지나왔다고 '.'으로 표시
            if isValidPos(x-1,y):stack.push((x-1,y)) # 상
            if isValidPos(x+1,y):stack.push((x+1,y)) # 하
            if isValidPos(x,y-1):stack.push((x,y-1)) # 좌
            if isValidPos(x,y+1):stack.push((x,y+1)) # 우
        print("현재 스택:" ,stack)
    return False

# 실행 코드
map = [ ['1','1','1','1','1','1'],
        ['0','0','0','0','0','1'],
        ['1','0','1','0','1','1'],
        ['1','1','1','0','0','x'],
        ['1','1','1','0','1','1'],
        ['1','1','1','1','1','1'] ]
MAX_SIZE = 6

result = DFS()
if result : print(' -->미로탐색 성공')
else : print('-->미로탐색 실패')        
