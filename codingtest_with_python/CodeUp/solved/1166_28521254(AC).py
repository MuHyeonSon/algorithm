﻿"""
2월이 29일까지 있는 해를 윤년이라고 한다.

한 자연수를 입력받아서 윤년인지 아닌지를 판단하는 프로그램을 작성하시오.

단, 윤년은 다음과 같은 성질을 지닌다고 한다.

(1) 400의 배수이면 무조건 윤년이다.
(2) (1)이 아닌 수 중에 4의 배수이며, 100의 배수가 아니면 윤년이다.

예)

2004 년 ====>  윤년(1번 조건)

2000 년 ====> 윤년 (2번 조건) 

1900 년 ====> 윤년 아님

1999 년 ====> 윤년 아님

입력
입력은 키보드로 이루어진다. 연도를 나타내는 자연수 n이 입력된다.
(단, 1<= n <= 2^32 - 1인 정수)

출력
입력받은 자연수가 윤년이라면 "Leap"를 아니라면 "Normal"을 출력한다.

입력 예시   
2012

출력 예시
Leap
"""
y = int(input())

if y % 400 == 0 :
    print("Leap")
elif (y % 4 == 0) and (y % 100 != 0) :
    print("Leap")
else:
    print("Normal")
