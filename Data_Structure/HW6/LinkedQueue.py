from Node import*

class LinkedQueue:
    def __init__ (self):
        self.front = None
        self.tail = None
        
        
    def isEmpty(self): return self.front == None##
    def clear(self):
        self.tail = None
        self.front = None ########
    def peek(self):
        if not self.isEmpty():
            return self.front.data####
    def enqueue(self,item):  # enqueue할 때는 tail 쪽으로만
        node = Node(item,None) # step1
        if self.isEmpty(): #########
            self.front = node
            self.tail = node
            
        else :
            self.tail.link = node
            self.tail = node
    
    def dequeue(self):      # dequeue할 때는 front 쪽으로만
        if not self.isEmpty():
            n = self.front
            self.front = n.link
    
    def size(self) : 
        node = self.front
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self,msg = 'LinkedQueue : '):
        print(msg,end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        
#테스트 프로그램
q = LinkedQueue()

print("0~7 정수 큐에 삽입")
for i in range(8): q.enqueue(i)
print(f'size: {q.size()}')
q.display()
print('\n')

print("큐에서 4개 삭제")
for i in range(4): q.dequeue()
print(f'size: {q.size()}')
q.display()
print('\n')

print("8~13 정수 큐에 삽입")
for i in range(8,14): q.enqueue(i)
print(f'size: {q.size()}')
q.display()

