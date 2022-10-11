"""
분수의 크기를 비교하는 프로그램을 작성하시오.

분수는 a / b  , c / d 모양으로 주어진다.

입력
a , b , c , d 가 차례대로 입력으로 주어진다.(자연수)

출력
a / b  >  c / d  이면  > 를 출력,

a / b =  c / d  이면  = 를 출력,

a / b  <  c / d  이면 < 를 출력.

입력 예시   
1 2 3 4

출력 예시
<
"""
a, b, c, d = map(int,input().split())
if (a / b) > (c / d) :
    print(">")
elif (a / b) < (c / d) :
    print("<")
elif (a / b) == (c / d) :
    print("=")
