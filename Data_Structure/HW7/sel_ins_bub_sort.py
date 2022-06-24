def printStep(arr,val):
    print("Step %2d   =  "%val, end='')
    print(arr) 
#선택정렬
def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i;
        for j in range(i+1,n):
            if (A[j]<A[least]):
                least = j
        A[i],A[least] = A[least],A[i]
        printStep(A,i + 1);
    print(f'Selection :  {A}')
#삽입정렬 (insertion sort)
def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A,i)
    print(f'Insert :     {A}')
#버블정렬 (bubble sort)
def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if(A[j]>A[j+1]):
                A[j],A[j+1] = A[j+1],A[j]
                bChanged = True
        if not bChanged: break;
        printStep(A,n-i);
    print(f'Bubble :     {A}')
#실습프로그램
while True:
    print('',end='\n')
    inp = int(input("1.선택정렬 2.삽입정렬 3.버블정렬 4. 종료 : "))
    Oroginal = [5,3,8,4,9,1,6,2,7]
    if inp == 4 :
        print("종료합니다!!")
        break;
    elif inp == 1:
        print(f'Oroginal :   {Oroginal}')
        selection_sort(Oroginal)
        
    elif inp == 2:
        print(f'Oroginal :   {Oroginal}')
        insertion_sort(Oroginal)
    
    elif inp == 3:
        print(f'Oroginal :   {Oroginal}')
        bubble_sort(Oroginal)
    else:
        print("잘못 선택하였습니다!!!")
        
    
