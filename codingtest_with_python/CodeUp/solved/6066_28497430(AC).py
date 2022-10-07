#1 2 8

#출력 예시
#odd
#even
#even

a, b, c = map(int,input().split())

for n in a,b,c:
    if (n % 2) == 0 :
        print("even")
    else:
        print("odd")
