

class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return str("%s:%s"%(self.key,self.value))
#순차 탐색(sequential)
def sequential_search(A, key, low, high) :
    for i in range(low,high+1): #low~high
        if A[i].key == key: # 탐색 성공하면
            if __name__ == '__main__':
                print(f'key={A[i].key} : value={A[i].value}')
                return i
            else:
                return i
    return None  #탐색에 실패하면 None 반환
#이진 탐색(binary search)
def binary_search(A,key,low,high):
    if (low <= high): #  항목들이 남아있는지 (종료조건)
        middle = (low + high) // 2
        if key == A[middle].key :
            print(f'key={A[middle].key} : value={A[middle].value}')
            return middle
        elif (key<A[middle].key):
            return binary_search(A,key,low,middle-1)
        else :
            return binary_search(A,key,middle+1,high)
    return None #탐색 실패 
#실습프로그램
#과제 세번째 문제에서 import할 때 이부분 실행 되지 않도록
if __name__ == '__main__':
    while True:
        print('',end='\n')
        inp = int(input("1.순차탐색 2.이진탐색 3.종료 : "))
        arr = [Entry(2,'a'),Entry(11,'b'),Entry(11,'c'),Entry(13,'d'),Entry(18,'e'),Entry(20,'f'),Entry(22,'g'),Entry(27,'h'),Entry(29,'i'),Entry(30,'j'),Entry(34,'k'),Entry(38,'l'),Entry(41,'m'),Entry(42,'n'),Entry(45,'o'),Entry(47,'p')]
        
        if inp == 1:
            for i in arr:
                print(i, end= ' ')
            print('',end='\n')
            sequential_search(arr,20,0,15)
        
        elif inp == 2:
            for i in arr:
                print(i, end= ' ')
            print('',end='\n')
            binary_search(arr,27,0,15)
    
        elif inp == 3 :
            print("종료합니다!!!")
            break;
    
        else:
            print("잘못 선택하였습니다!!!")