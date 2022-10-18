"""
어떤 문자열이 있을 때 문자 t의 위치를 모두 찾아 출력하시오.

입력
공백이 없는 문자열이 한 줄 입력된다.(10글자 이하)

출력
소문자 t의 위치를 공백으로 분리하여 모두 출력하시오.

입력 예시   
test

출력 예시
1 4 
"""

input_string = input() # 문자열 입력받음
input_list = [x for x in input_string] # 입력받은 문자열에서 문자 하나씩 원소로 한 리스트 생성

for i in range(len(input_list)):
    if input_list[i] == 't': # i 번째 문자가 't'라면
        print(str(i+1), end = ' ') # t의 위치 출력



