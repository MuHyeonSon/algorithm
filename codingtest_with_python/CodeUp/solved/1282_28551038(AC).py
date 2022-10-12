"""
n이 입력되면 k를 빼서 제곱수를 만들 수 있는 k를 구하고,

그 제곱수에 루트를 씌운 수(제곱근) t를 구하여라.

이 때 k는 여러가지가 될 수 있는데 가장 작은 k를 출력한다.

입력
n이 입력된다.(0<k<n<=231)

출력
k와 t를 출력한다. 이 때 k는 여러가지가 될 수 있는데 가장 작은 k를 출력한다.

입력 예시   
34

출력 예시
9 5
"""
import math
n = int(input())
k = 0
t = 0
for i in range(1,n):
    if float(math.sqrt(n - i)).is_integer() :
      t = int(math.sqrt(n - i))
      k = i
      break
print(k,int(t))
        
    
