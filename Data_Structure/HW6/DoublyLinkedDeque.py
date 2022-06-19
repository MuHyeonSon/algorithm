from DNode import*

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self): return self.front == None #공백상태 검사
    def clear(self) : self.front = self.front = None
    def size(self) : 
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count
    def display(self,msg = 'DoublyLinkedDeque : '):
        print(msg,end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()
    def addFront(self,item):
        node = DNode(item, None, self.front) # step1
        if (self.isEmpty()):
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data #step1
            self.front = self.front.next # step2 
            if self.front == None : #노드가 하나 뿐이면
                self.rear = None    #rear도 None으로 설정
        else:
            self.front.prev = None  #step3
        return data                 #step4
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data  #step1
            self.rear = self.rear.prev #step2
            if self.rear == None : #노드가 하나 뿐이면
                self.front = None  #front도 None으로 설정
            else:
                self.rear.next = None      #step3
        return data   #step4
    
#테스트 프로그램
dq = DoublyLinkedDeque()
for i in range(9):
    if i%2 == 0 : dq.addRear(i)
    else: dq.addFront(i)
dq.display()

for i in range(2) : dq.deleteFront()
for i in range(3) : dq.deleteRear()
dq.display()

for i in range(9,14): dq.addFront(i)
dq.display()
            