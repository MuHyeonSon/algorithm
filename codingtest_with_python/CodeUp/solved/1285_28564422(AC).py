"""
계산기 1에서 두 피연산자에 대한 연산만 다루었다.

이번에는 식을 입력하면 차례대로 계산하여 출력하는 계산기를 만들어보자.

단, 우선순위는 따지지 않고 왼쪽에서 부터 차례대로 계산하고, 모든 계산은 정수형 계산으로 처리한다.

입력
첫째 줄에 정수와 사칙연산기호가 식으로 입력된다.

(정수는 int 범위, 괄호 없이 +,-,*,/) 

식의 마지막엔 =가 입력된다.

출력
왼쪽부터 차례대로 연산한 결과를 출력한다.(우선순위x)

입력 예시   
3+3-3*3/3=

출력 예시
3
"""
calc_list = []
calc_express = input()
temp_digit = ''
# 숫자와 식 구분해서 각 연산자 및 피연사자를 리스트에 저장(한 자리수 이상도 가능)
for x in calc_express: # 숫자랑 식 나눠서 순서대로 리스트 순서에 넣기
    if x.isdigit(): # 만약 숫자라면
        temp_digit = temp_digit + x
    else:
        calc_list.append(int(temp_digit))
        calc_list.append(x)
        temp_digit = ''

# 리스트에 저장된 연산자 및 피연산자들을 하나씩 꺼내서 결과 값 계산
result = 0
temp_rdigit = 0
temp_ldigit = 0
temp_calc = ''

result = calc_list[0]
#print(result)
#print(calc_list)
for x in range(1,len(calc_list)):
#    print(f'calc_list[{x}] : {calc_list[x]}')
#    print(f'result : {result}')
    if str(calc_list[x]).isdigit(): # 피연산자라면
        d = int(calc_list[x]) # 문자열 형식일테니 정수형으로 바꿔주고
        if temp_calc == '+': # 연산자가 + 였다면
            result += d
        elif temp_calc == '-':
            result -= d
        elif temp_calc == '*':
            result *= d
        elif temp_calc == '/':
            result /= d
            result = int(result)
        elif temp_calc == '=':
            break
    else: # 연산자라면
        temp_calc = calc_list[int(x)]
print(int(result))
    
"""
for x in calc_list:
    if x.isdigit(): # 리스트에서 꺼낸 원소가 숫자라면
        if temp_calc == '' # 연산자가 빈 연산자면
            temp_ldigit = x
        else:
            temp_rigit = x
            temp_calc = ''
            
            
    else: # 리스트에서 꺼낸 원소가 숫자가 아니라면
        temp_calc = x
"""    
    
    
    
