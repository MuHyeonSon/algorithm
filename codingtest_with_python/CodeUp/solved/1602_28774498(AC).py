﻿"""
절대값 함수를 만들어 봅시다.

입력으로 정수가 들어오면 정수로 결과를 출력하고, 실수가 들어오면 실수로 결과를 출력한다.

단, 소수점 이하에 불필요한 0은 입력되지 않는다.

[리턴 타입] ABS( [인자] )

{

        // ..코드..

}

int main()

{

       // 명령 및 함수 호출

}

입력
정수 또는 실수 n이 입력된다. (n은 정수 또는 실수)

출력
입력된 n의 절대값을 출력한다.

실수값일 경우 불필요한 0을 출력하지 않는다.

입력 예시   
-2.56

출력 예시
2.56
"""

v = float(input())

def absolute_value(n):
    if n.is_integer():
      return(int(abs(n)))
    else:
      return(abs(n))
    
    
print(absolute_value(v))

