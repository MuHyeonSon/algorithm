from CircularQueue import * # 원형 큐 클래스 import

s = CircularQueue() # 원형큐를 사용하기 위해 객체 선언


s.enqueue(0)   #f(0)
s.enqueue(1)   #f(1)

print(f'피보나치 수열 : {s.peek()} ', end='')
for i in range (10):
    a = s.dequeue()   #f(n-2)
    b = s.peek()      #f(n-1)    그 다음 연산에서 사용해야하므로 꺼내지 않음
    c = b + a         #f(n) = f(n-1) + f (n-2)
    s.enqueue(c)      #삽입
    d = s.peek()
    print(d, end=' ') # 각 결과를 줄바꿈을 제거하여 붙여서 출력


