"""
길이(글자수)가 100이하인 문자열을 입력받아 공백을 제거하고 출력하시오.

입력
문자열이 입력된다.(글자 수는 100글자 이하이고, 알파벳 대소문자와 공백 문자만 입력된다.)

출력
공백을 제거한 후 출력한다.

입력 예시   
abC Def gh

출력 예시
abCDefgh
"""

input_string = input()
output_string = input_string.replace(' ','')
print(output_string)
