"""
대영이는 SNS를 이용한 컨설팅 회사를 운영하고 있다. 

이 회사에서 획기적인 기획안을 개발하여 사람들에게 홍보를 하려고 한다.

홍보를 할 경우 수입과 그렇지 않을 경우의 수입을 알고 있을 경우, 

홍보를 하는 경우가 유리한가?

홍보를 하지 않은 경우가 유리한가?

그것도 아니면 홍보를 하든 안하든 별 관계가 없는가?

이것을 알아내는 프로그램을 만드시오.

입력
입력으로 세 정수가 입력된다. 

첫번째 정수는 홍보를 하지 않을 경우 수입,

두번째 정수는 홍보를 할 경우의 수입,

세번째 정수는 홍보비용을 의미한다.

출력
홍보를 하는 경우가 유리하면 "advertise"

그렇지 않은 경우가 유리하면 "do not advertise"

그것도 아니면 홍보를 하든 안 하든 별 관계가 없으면 "does not matter"

를 출력하시오.

입력 예시   
10 100 70

출력 예시
advertise
"""
income_no_ad, income_ad, expenses = map(int,input().split())
# 홍보를 할 경우의 수입에서 홍보비용을 뺀 금액이 홍보를 하지 않을 경우 수입보다 크다면 홍보가 유리
if income_ad - expenses > income_no_ad :
    print("advertise")
elif income_ad - expenses == income_no_ad:
    print("does not matter")
else:
    print("do not advertise")
