"""
서브 스트링 함수는 문자열 처리에 있어 아주 유용한 함수이다.(엑셀이나 VB에선 Mid함수)

이 함수는 원본 문자열에서 특정위치에서 부터 몇 글자를 추출하는 함수이다.

이 함수를 직접 구현해보자.


입력
첫째 줄에 문자열이 공백없이 입력된다.(문자열은 100글자 이하)

둘째 줄에 문자열의 시작위치와 글자 개수가 입력된다.

(첫글자는 시작위치가 0이다. 글자개수는 시작위치부터 출력할 글자 수를 의미한다.)

출력
결과를 출력한다.

입력 예시   
abcdefg
2 3

출력 예시
cde
"""

def sub_string(string,s,l):
    return string[s:s+l]


input_str = input()
start, length = map(int,input().split())

print(sub_string(input_str,start,length))
