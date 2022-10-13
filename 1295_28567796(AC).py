"""
주어지는 문장의 대문자를 소문자로, 소문자를 대문자로 변경하는 프로그램을 작성하라.

입력
한 줄의 공백없는 문장이 입력된다.(최대 길이:1000)

출력
대소문자를 서로 변환한 결과를 출력한다.

입력 예시   
CodeChallenge2014withMSP

출력 예시
cODEcHALLENGE2014WITHmsp
"""
# 각 맵핑되는 알파벳 문자 소문자 대문자를 ord() 함수 사용해서 아스키값 변환했을 때 얼마씩 차이나는 지 알면 구할 수 있음
difference = ord('a') - ord('A')

input_str = input()
output_str = '' 

for x in input_str:
    if not x.isalpha(): # 알파벳이 아니라면 그냥 갖다 붙임
        output_str = output_str + x
    else: # 알파벳 문자면 대문자는 소문자로, 소문자는 대문자로 바꿔서 갖다 붙임
        if x.isupper() : # 대문자면
            x = chr(ord(x) + difference) # 소문자로 바꿔줌
            output_str = output_str + x
        else: # 소문자면
            x = chr(ord(x) - difference)
            output_str = output_str + x
            
print(output_str)
