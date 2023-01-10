# condingtest_with_python_part3_Greedy
# 곱하기혹은더하기.py


# 나의 풀이 (교재 해설 참고)
S = input()
result = int(S[0])

for i in range(1, len(S)):
    n = int(S[i])
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)



# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 20분 17.21초)

"""
import math

S = str(input())

cal = ''

result = ""

for i in range(len(S)):
    if i-1 > -1 and int(S[i-1]) == 0:
        result += S[i] + ")"
        continue
    if int(S[i]) == 0:
        result += "(" + S[i] + "+"
    else:
        result += "*" + S[i]    
if result[0] == "*":
    result = result[1:]
#print(result)
print(eval(result))

"""

# 교재 풀이




# 느낀점
"""
죽을만큼 비효율적으로 풀었다.. 문자열 처리할 필요없이 그냥 하나씩
더하거나 곱하면 되는 거였는데, 완전히 이상하게 풀었다.
일단 문제 만나면 최대한 간단하게 생각해보자
그리고 그리디 알고리즘에서의 해법을 생각함으로서 내가 놓쳤던 부분은
다음과 같다.

1. 문자 하나가 0 이었을 경우에는 곱하는 것보다 더하는 것이 낫다 -> 생각함
문자 하나가 1이었을 경우 곱하는 거보다 더하는게 낫다 -> 생각못함
1을 곱하면 그 숫자 그대로지만 더하면 1이라도 커지기 때문인데
이것을 생각하지 못했다.

2. 첫 문자는 어차피 처리해야될 수 이므로 그냥
처음부터 첫 문자 값으로 result를 초기화하면 되는 거였다.  
"""
