"""
다음과 같은 n*m 배열 구조를 출력해보자.

입력이 3 4인 경우 다음과 같이 출력한다.
12 11 10 9
5 6 7 8
4 3 2 1

입력이 4 5인 경우는 다음과 같이 출력한다.
16 17 18 19 20
15 14 13 12 11
6 7 8 9 10
5 4 3 2 1

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
4 5 6 
3 2 1 
"""

n, m = map(int, input().split())

cnt_loop = 0

if n == 1 and m == 1 :
  print(1)
else :
    if n % 2 == 0: # n이 짝수라면
        for i in range(n,0,-1):
            for j in range(m):
                if cnt_loop % 2 != 0 : # 짝수 번째 행이라면 내림차순
                    print((i*m) - (j), end = ' ')
                              
                else : # 홀수 번째 행이라면 오름차순
                  if m == 1:
                    print((i*m), end = ' ')
                  else:
                    print((i*m) - (m-(j+1)), end = ' ')
            
            print()
            cnt_loop += 1
    
    else: # n이 홀수라면
        for i in range(n,0,-1):
            for j in range(m):
                if cnt_loop % 2 != 0 : # 짝수 번째 행이라면 오름차순
                  if m == 1:
                    print((i*m), end = ' ')
                  else:
                    print((i*m) - (m-(j+1)), end = ' ')
                              
                else : # 홀수 번째 행이라면 내림차순
                    print((i*m) - (j), end = ' ')
            
            print()
            cnt_loop += 1
        
