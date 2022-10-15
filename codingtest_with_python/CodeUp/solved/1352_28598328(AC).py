"""
길이 n이 입력되면 길이가 n인 사각형을 출력하시오.

단, 사각형은 * 모양으로 채운다.

입력
사각형의 길이 n이 입력된다.

출력
가로 세로 길이 n인 사각형을 출력한다.

입력 예시   
4

출력 예시
****
****
****
****
"""
# 이렇게도 가능
n = int(input())
for _ in range(n):
    print('*'*n)
    
# 중첩 반복문으로 구현하면
"""
n = int(input())
for _ in range(n):
  for _ in range(n):
    print('*', end = '')
  print()
"""
    
