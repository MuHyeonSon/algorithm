from PriorityQueue import *
import math

def isValidPos(x,y):
      if x<0 or y<0 or x>= MAX_SIZE or y>=MAX_SIZE:
          return False
      else :
          return map[x][y]=='0' or map[x][y]== 'x'

(ox,oy) = (4,5)   #출구의 위치

def dist(x,y):
  (dx,dy) = (ox-x,oy-y)
  return math.sqrt(dx*dx + dy*dy)

def smartSearch():
  q = PriorityQueue()
  q.enqueue((1,0,-dist(1,0)))
  print("PQueue:")

  while not q.isEmpty():
    here = q.dequeue()
    print(here[0:2],end='->')
    x,y,_ = here
    if map[x][y] == 'x': return True
    else : 
      map[x][y]='.'
      if isValidPos(x-1,y) : q.enqueue((x-1,y,-dist(x-1,y)))
      if isValidPos(x+1,y) : q.enqueue((x+1,y,-dist(x+1,y)))
      if isValidPos(x,y-1) : q.enqueue((x,y-1,-dist(x,y-1)))
      if isValidPos(x,y+1) : q.enqueue((x,y+1,-dist(x,y+1)))
      print("우선순위큐:",q.items)
    
  return False

map = [['1','1','1','1','1','1'],
       ['0','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]

(ox,oy) = (4,5)
MAX_SIZE = 6

res=smartSearch()
if res : print('-->미로탐색 성공!')
else : print('-->미로탐색 실패!')
