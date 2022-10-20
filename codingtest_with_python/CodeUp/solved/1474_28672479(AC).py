"""
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
10 9 4 3
11 8 5 2
12 7 6 1

입력이 4 5인 경우는 다음과 같이 출력한다.
20 13 12 5 4
19 14 11 6 3
18 15 10 7 2
17 16 9 8 1

입력이 n m인 경우의 2차원 배열을 출력해보자.

입력
첫 번째 줄에 배열의 크기 n m이 입력된다.
[입력값의 정의역]
1<=  n,m <= 100

출력
n*m 크기의 배열을 설명과 같이 채워 출력한다.

입력 예시   
2 3

출력 예시
6 3 2 
5 4 1 
"""

n, m = map(int, input().split())

if n == 1 and m == 1 :
  print(1)
else :
    if m % 2 == 0: # m이 짝수라면
        for i in range(n):
            for j in range(m):
                if j % 2 == 0 : # 홀수 번째 열이라면 내림차순
                  if m == 1:
                    print((n*m) - i, end = ' ')
                  else:
                    print((n*m) + i - (j*n) - (n-1), end = ' ')                             
                else : # 짝수 번째 열이라면 오름차순
                    print((n*m) - i - (j*n), end = ' ')           
            print()
    else : # m이 홀수라면
        for i in range(n):
            for j in range(m):
                if j % 2 == 0 : # 홀수 번째 열이라면 오름차순
                  if m == 1:
                    print((n*m) - i, end = ' ')
                  else:
                    print((n*m) - i - (j*n), end = ' ')
                              
                else : # 짝수 번째 열이라면 내림차순
                  print((n*m) + i - (j*n) - (n-1), end = ' ')            
            print()

