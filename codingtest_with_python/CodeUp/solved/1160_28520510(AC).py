﻿"""
주원이는 월, 수, 금, 일 아르바이트를 간다.

다음은 요일의 순서이다.

1월요일
2화요일
3수요일
4목요일
5금요일
6토요일
7일요일
요일의 번호가 입력으로 주어지면 그 날이 아르바이트 가는 날이면 "oh my god"를 가는 날이 아니면 "enjoy"를 출력하시오.

입력
입력으로 요일의 번호가 하나 주어진다.(정수)

출력
 아르바이트 가는 날이면 "oh my god"를 가는 날이 아니면 "enjoy"를 출력하시오.

입력 예시   
1

출력 예시
oh my god
"""
n = int(input())
if n == 1 or n == 3 or n == 5 or n == 7:
    print("oh my god")
else:
    print("enjoy")