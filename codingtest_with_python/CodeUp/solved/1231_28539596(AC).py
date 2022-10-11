"""
영민이는 프로그램을 이용하여 계산기를 만들려고한다.

하지만 영민이는 프로그램을 얼마 배우지 않아 어려워하고있다.

우리가 영민이를 위해 계산기 프로그램을 만들어주자.

입력
연산식이 한줄로 입력된다.

연산식의 형식은 정수+정수 또는 정수-정수 또는 정수*정수 또는 정수/정수의 형태이다.

 

출력
계산 결과를 정수로 출력한다.

나눗셈일 경우 실수로 출력하되 소수 둘째자리까지 출력한다.

(0으로 나누는 경우는 입력되지 않는다.)

입력 예시   
10+10

출력 예시
20
"""
expression = input()
if '+' in expression :
    index_operation = expression.find('+')
    source = int(expression[0:index_operation])
    target = int(expression[index_operation+1:])
    print(source + target)
elif '-' in expression :
    index_operation = expression.find('-')
    source = int(expression[0:index_operation])
    target = int(expression[index_operation+1:])
    print(source - target)
    
elif '*' in expression :
    index_operation = expression.find('*')
    source = int(expression[0:index_operation])
    target = int(expression[index_operation+1:])
    print(source * target)
elif '/' in expression :
    index_operation = expression.find('/')
    source = int(expression[0:index_operation])
    target = int(expression[index_operation+1:])
    print(f'{(source / target):.2f}')


