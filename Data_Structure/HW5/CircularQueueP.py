from CircularQueue import *

from BFS import *

map = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]

MAX_SIZE = 6
result = BFS()
if result : print('-->미로탐색 성공!')
else : print('-->미로탐색 실패!')
