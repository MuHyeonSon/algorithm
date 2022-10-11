"""
영어로 서수를 표현할 때 다음과 같이 나타낸다.

1st  2nd  3rd  4th  5th  6th  ... 10th

11th 12th 13th 14th 15th  ...  20th

21st 22nd 23rd 24th 25th  ...  30th

31st 32nd 33rd 34th 35th  ...  40th

41st 42nd 43rd 44th 45th  ...  50th

...

91st 92nd 93rd 94th 95th  ...  99th

1~99 중 하나가 숫자가 입력되면 영어 서수 표현을 출력하시오.
"""
n =input()
if 10 <= int(n) <= 20 : # 10부터 20 숫자는 전부 뒤에 th가 붙으므로
    print(n+'th') 
else: # 그외에 숫자들
    if n[-1] == '1': # 1의 자리가 1이라면
        print(n+'st')
    elif n[-1] == '2': # 1의 자리가 2이라면
        print(n+'nd')
    elif n[-1] == '3': # 1의 자리가 3이라면
        print(n+'rd')
    else:
        print(n+'th')
