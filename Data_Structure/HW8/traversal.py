from CircularQueue import*

class TNode:
    def __init__(self,data,left,right):
        self.data = data 
        self.left = left
        self.right = right
        

# 전위 순회
def preorder(n):
    if n is not None:
        print(n.data,end='')
        preorder(n.left)
        preorder(n.right)
#중위 순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data,end='')
        inorder(n.right)
#후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data,end='')
        
#레벨 순회
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data,end='')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
            
#노드 개수 (순환을 이용해 트리의 노드 수를 계사하는 함수)
def count_node(n):
    if n is None: # n이 None이면 공백 트리 --> 0을 반환
        return 0 
    else :        # 좌우 서브트리의 노드 수의 합 + 1 
        return 1 + count_node(n.left) + count_node(n.right)
    
#단말 노드의수 
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right) 
# 트리의 높이
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight) :
        return hLeft + 1
    else:
        return hRight + 1   
# 테스트 프로그램
d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',f,None)
root = TNode('A',b,c)
print('\n   In-Order : ', end='')
inorder(root)
print('\n  Pre-Order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()
print("노드의 개수 = %d개" % count_node(root))
print("단말의 개수 = %d개" % count_leaf(root))
print("트리의 높이 = %d" % calc_height(root))

 

            