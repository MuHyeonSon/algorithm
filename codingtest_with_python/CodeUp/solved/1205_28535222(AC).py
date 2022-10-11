"""
두 실수 a, b가 입력되면 그 두수를 더하거나 빼거나 곱하거나 나누거나 제곱을 해서 가장 큰 수를 출력하시오.

예를 들어 1과 2가 입력되면,

1+2 = 3   , 2+1 = 3

1 - 2 = -1,   2 - 1 = 1

1 * 2 = 2,    2 * 1 = 2

1 / 2 = 0.5,   2 / 1 = 2

12=1 ,   21 = 2

따라서 최댓값은 3이다.
"""
a, b = map(int,input().split())
add = a + b 
sub1 = a - b
sub2 = b - a
mul = a * b
dev1 = float(a / b)
dev2 = float(b / a)
sqr1 = a ** b
sqr2 = b ** a
#최댓값을 소수점이하 6자리로 출력한다.
print(f'{max(add,sub1,sub2,mul,dev1,dev2,sqr1,sqr2):.6f}')
