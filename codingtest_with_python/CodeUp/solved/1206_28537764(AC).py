"""
두 자연수 a, b가 주어진다.

b가 a의 배수이면 "a*x=b"를 출력하고,

a가 b의 배수이면 "b*x=a"를 출력하고,

배수관계가 아니면 "none"을 출력하시오.

예) 

5 10    ====> 5*2=10

14 2   ======> 2*7=14

3 7 =====> none

입력
자연수 두 개가 입력된다.

출력
위의 문제 설명을 보고 배수 관계를 출력한다.

입력 예시   
4 12

출력 예시
4*3=12
"""
# 배수 관계임은 어떻게 알 수 있나 -> 나누기 연산 했을 때 몫이 1이상이고 소수점이 첫째자리가 0 이면 배수 관계?
# -> 아니다.. 그냥 나머지가 0이면 배수잖아
a, b = map(int,input().split())
if a >= b:
  if a % b == 0: 
      print(str(b)+'*'+str(a//b)+'='+str(a))
  else :
      print('none')
else:
  if b % a == 0 : 
      print(str(a)+'*'+str(b//a)+'='+str(b))
  else :
      print('none')
"""
a, b = map(int,input().split())
if a >= b:
  #print(f"str(a/b)[(str(a/b).find('.')) + 1] : {str(a/b)[(str(a/b).find('.')) + 1]}")
  if ((a/b) >= 1) and str(a/b)[(str(a/b).find('.')) + 1] == '0' : # find 함수 사용하여 나누기 결과에 점에 오른쪽 숫자의 인데스를 찾음
      print(str(b)+'*'+str(a//b)+'='+str(a))
  else :
      print('none')
else:
  #print(f"str(b/a)[(str(b/a).find('.')) + 1] : {str(b/a)[(str(b/a).find('.')) + 1]}")
  if ((b/a) >= 1) and str(b/a)[(str(b/a).find('.')) + 1] == '0' : # find 함수 사용하여 나누기 결과에 점에 오른쪽 숫자의 인데스를 찾음
      print(str(a)+'*'+str(b//a)+'='+str(b))
  else :
      print('none')
"""

