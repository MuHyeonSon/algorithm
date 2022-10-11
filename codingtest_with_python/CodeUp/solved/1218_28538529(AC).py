"""삼각형의 3변의 길이 a, b, c가 입력으로 주어진다.

여기서 입력되는 변의 관계는 a ≤ b ≤ c 이다. 

그 삼각형이 무슨 삼각형인지 출력하시오.

입력
변의 길이 a, b, c가 입력된다. ( 정수)

출력
조건에 따라 삼각형을 출력한다.

조건)

세 변의 길이가 같은 경우 : 정삼각형

두 변의 길이가 같은 경우 : 이등변삼각형

a2 + b2 = c2일 경우(피타고라스 정리) : 직각삼각형

위의 조건에 맞지 않는 일반 삼각형일 경우 : 삼각형

삼각형이 아닐 경우 : 삼각형아님

을 출력한다."""

lengths = list(map(int,input().split()))
lengths.sort()
if lengths[2] >= lengths[0] + lengths[1]:
    print("삼각형아님")
else :
    if (lengths[0] == lengths[1]) and (lengths[0] == lengths[2]):
        print("정삼각형")
    elif (lengths[0] == lengths[1]) or (lengths[0] == lengths[2]) or (lengths[1] == lengths[2]):
        print("이등변삼각형")
    elif lengths[2] ** 2 == (lengths[0] ** 2) + (lengths[1] ** 2):
        print("직각삼각형")
    else:
        print("삼각형")
