"""
영어 문장이 입력된다.

그 문장에서 love가 몇 번 나오는지 출력하시오.

입력
영어 한 문장이 입력된다.(공백 있음, 최대 글자수 100)

출력
소문자 love가 몇 번 나오는지 출력한다.

입력 예시   
love lovely

출력 예시
2
"""

input_string = input()

print(input_string.count('love'))
