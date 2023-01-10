# condingtest_with_python_part3_구현
# 문자열재정렬.py

# 나의 풀이 (교재 해설 참고)

s = input()
result = []
value = 0

for c in s:
    if c.isdigit(): # 만약 알파벳인지 확인하면 isalpha()
        value += int(c)
    else:
        result.append(c)

## 알파벳을 오름차순으로 정렬
result.sort()

## 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
## 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))


# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 7분 51.61초)
"""
s = input()
total_number = 0
alpha = []
result_s = ''

for c in s:
    if c.isdigit():
        total_number += int(c)
    else:
        alpha.append(c)
alpha.sort()
for c in alpha:
    result_s += c
print(result_s + str(total_number))
"""

# 느낀점
"""
어렵지 않게 풀 수 있었지만 해설을 보니
따로 결과를 저장할 문자열 변수 선언하지 않았어도 되었다.
또한 문제에서 따로 언급이 없어 숫자를 모두 더한 값이 0인 경우에도
문자열뒤에 0을 붙이는 것으로 코드를 작성했다.

알게 된 점
1. print(''.join(리스트)) 형태로 작성하면 리스트를 문자열로 변환하여 출력할 수 있다.

"""
