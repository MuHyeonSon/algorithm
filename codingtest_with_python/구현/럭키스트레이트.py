# condingtest_with_python_part3_구현
# 럭키스트레이트.py


# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 20분, 풀이 시간 : 11분 37.79초)

## 캐릭터의 점수 입력받기
N = int(input())
N_list = []

for n in str(N):
    N_list.append(int(n))

len_N = len(str(N))    
if sum(N_list[:len_N // 2]) == sum(N_list[len_N//2:]):
    print("LUCKY")
else:
    print("READY")

# 교재 풀이
n = input()
length = len(n)
summary = 0

## 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

## 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

## 왼쪽부분과 오른쪽부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
    
# 느낀점
"""
교재 풀이를 보며 합과 차를 계산해 나온 값이 0인지를 판별함으로써 왼쪽부분과 오른쪽부분이 같은지를
검사하는 방법이 새로웠고, 문제에서 정수형 입력이 주어진다고 해서 무조건 이 것을 지킬 필요가 없다는
것도 느끼게 되었다.
"""

"""
📰 Codingtest_with_python_part3_구현_럭키스트레이트
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 구현 문제 풀이 느낀점
"""
