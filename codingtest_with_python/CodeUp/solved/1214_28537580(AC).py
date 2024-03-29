﻿"""
철수와 영희는 한 사람이 특정 월(month)을 지목하면 나머지 사람이 그 달의 마지막 날이 며칠인지 알아맞히는 게임을 하였다. 두 사람 모두 처음엔 서툴렀지만 게임을 계속하다 보니 금방 익숙해졌다. 그래서 게임의 규칙을 조금 어렵게 바꿔 연도와 월을 말하면 그 달의 마지막 날이 며칠인지 알아맞히기로 하였다.

이 규칙이 어려운 이유는 2월이 윤달이 있기 때문이다.

2월이 29일인 해를 윤년이라고 하는데, 윤년의 판단은 아래 두 조건 중 하나만 만족하면 된다.

- 조건 1 : 400의 배수인 해는 모두 윤년이다.

- 조건 2 : 4의 배수인 해들 중 100의 배수가 아닌 해들은 모두 윤년이다.

연도와 월을 알고 있을 때 그 달의 마지막 날을 구하는 프로그램을 작성하시오.

<참고> 월별 마지막 날

입력
연도와 월이 입력된다.

출력
그 달의 마지막 날이 며칠인지 출력한다.

입력 예시   
2009 10

출력 예시
31
"""
y, m = map(int,input().split())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if m == 2: # 2월일 경우 윤년인지 판단해야 됨
    if ((y % 400) == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        print(29)
    else:
        print(28)
else:
    print(days[m])
"""        
else:
    if m == 1 :
        print(31)
    elif m == 3 :
        print(31)
    elif m == 4 :
        print(30)
    elif m == 5 :
        print(31)
    elif m == 6 :
        print(30)
    elif m == 7 :
        print(31)
    elif m == 8 :
        print(31)
    elif m == 9 :
        print(30)
    elif m == 10 :
        print(31)
    elif m == 10 :
        print(31)
    elif m == 10 :
        print(31)
"""        
    
