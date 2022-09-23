#boj 24416 손무현
"""
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
입력
첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.

출력
코드1 코드2 실행 횟수를 한 줄에 출력한다.

예제 입력 1 
5
예제 출력 1 
5 3
"""

count_code1 = 0
count_code2 = 0

def fibonacci_recursive(n): # 재귀호출을 이용한 피보나치 수 계산 함수
  global count_code1

  if (n == 1) or (n == 2):
    count_code1 += 1 
    return 1 #코드1
  else : 
    return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

def fibonacci_DP(n): # Dynamic programming을 이용한 피보나치 수 계산
  global count_code2
  global f

  for i in range(2,n):
    f[i] = f[i - 1] + f[i - 2]  # 코드2
    count_code2 += 1
  
#main

n = int(input())

f = [1]*n

fibonacci_recursive(n) # 재귀함수를 이용한 피보나치 수 계산
fibonacci_DP(n) # Dynamic programming을 이용한 피보나치 수 계산

print(count_code1,count_code2) # 코드1과 코드2 실행 횟수 출력
