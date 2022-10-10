"""
인학이는 숫자 7을 좋아한다.

어떤 정수가 입력되면 그 수가 7의 배수인지 확인하시오.
7의 배수일 경우 multiple를 출력하고, 7의 배수가 아니면 not multiple을 출력하시오.
"""

n = int(input())

if n % 7 == 0:
    print("multiple")
else:
    print("not multiple")
