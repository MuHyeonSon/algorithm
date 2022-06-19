from Node import *

class CircularLinkedQueue:
    def __init__ (self):
        self.tail = None
        
    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self,item):
        node = Node(item,None) # step1
        if self.isEmpty():
            node.link = node #step2
            self.tail = node #step3
        else :
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data #step1
            if self.tail.link == self.tail :
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
    def size(self):
        if self.isEmpty() : return 0 # 공백이면 0반환
        else :
            count = 1
            node = self.tail.link #node는 front부터 출발
            while not node == self.tail: #node가 rear가 아니면(tail이 아닐 때까지 반복)
                node = node.link
                count += 1
            return count
    def display(self, msg= 'CircularLinkedQueue : '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link # 리스트의 맨 앞으로 이동
            while not node == self.tail:
                print(node.data,end=' ')
                node = node.link
            print(node.data,end=' ') #마지막 노드의 항목 출력
        print()
        
#테스트 프로그램
q = CircularLinkedQueue()

for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8,14): q.enqueue(i)
q.display()
            
                