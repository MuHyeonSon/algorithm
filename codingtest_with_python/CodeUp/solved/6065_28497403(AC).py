#3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a, b, c = map(int,input().split())

for n in a, b, c:
    if (n % 2) == 0:
        print(n)
        

