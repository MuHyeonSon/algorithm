"""
세 개의 직선이 있다.

숫자의 의미는 직선의 길이를 말한다.

이 직선으로 삼각형을 만들 수 있는지 판단하는 프로그램을 작성하시오.

삼각형의 성립 조건)

a, b, c 가 변의 길이이고 c가 제일 긴 길이라고 한다면

c < a + b 이면 삼각형이 성립됨.

입력
직선의 길이 3개가 입력으로 주어진다.(정수)

출력
삼각형이 가능하면 "yes", 삼각형을 만들 수 없다면 "no"를 출력하시오.
"""
lengths = list(map(int,input().split()))
lengths.sort()
if lengths[2] < lengths[0] + lengths[1] :
    print("yes")
else:
    print("no")

