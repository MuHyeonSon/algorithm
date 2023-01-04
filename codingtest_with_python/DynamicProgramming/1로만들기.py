# condingtest_with_python_part2_다이나믹_프로그래밍
# 1로만들기.py
## 정수 X가 주어졌을 때 연산 사용하는 횟수를 최소로 하여 1만들기 -> 연산횟수의 최솟값을 출력

# 나의 풀이

## 반복적 방법 써보자(DP테이블)
## DP테이블의 기록해야되는 것은 4가지 연산에 대한 연산 수행 결과 일것임
## 2차원 테이블 만들어서 각 숫자에 대해 연산 결과 기록하고 연산 후 숫자에 대한 4가지 연산 후 결과를 또 기록함 1이 발견되면 거기서 멈추고 연산 횟수를 출력


## 정수 입력
x = int(input())

def make_one(x):
  DP_Table = [0]
  count_of_calculation = 0
  find = False
  while not find:
    x = DP_Table[-1]
    current_result = [0] * 4
    # 연산 a : x가 5로 나누어떨어진다면 5로 나눈다.
    if x % 5 == 0 and x >= 1 :
      a = x
      a = a // 5
      DP_Table.append(a)
      #current_result[0] = a
    # 연산 b : x가 3으로 나누어떨어진다면 2로 나눈다.
    elif x % 3 == 0 and x >= 1 :
      a = x
      a = a // 3
      DP_Table.append(a)
      #current_result[1] = a
    # 연산 c : x가 2로 나누어떨어진다면 3로 나눈다.
    elif x % 2 == 0 and x >= 1 :
      a = x
      a = a // 2
      DP_Table.append(a)
      #current_result[1] = a
    # 연산 d : x에서 1을 뺀다.
    elif x - 1 >= 1:
      a = x
      DP_Table.append(a)

    count_of_calculation += 1
    if DP_Table[-1] == 1:
      find = True
      return count_of_calculation
      
print(make_one(x))

  




# 나의 풀이 (최종)

# 교재 풀이
## 정수 x 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp_table = [0] * 30001 # (1<= x <=30000)

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
for i in range(2, x + 1):
  # 현재의 수에서 1을 빼는 경우
  dp_table[i] = dp_table[i - 1] + 1 # i를 1로 뺀 수를 만들기 위한 최소 연산 횟수와 현재 이 연산을 함으로써 발생하는 연산횟수 1을 더함
  # 현재의 수가 2로 나누어 떨어지는 경우
  if i % 2 == 0:
    dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
  # 현재의 수가 3으로 나누어 떨어지는 경우
  if i % 3 == 0:
    dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
  # 현재의 수가 5로 나누어 떨어지는 경우
  if i % 5 == 0:
    dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)
  
print(dp_table[x])
  

# 느낀점
"""
교재에서는 피보나치 수열 문제 DP로 풀었던 방법을 잘 알아두면
다른 DP 문제에 접근하는 방법 또한 떠올릴 수 있을 거라고 말했지만,
아직 그러지 않은 것 같다. 풀이시간20분이었고 25분동안 생각해보고
구현 해보았지만 끝내 해결하지 못했다. 뾰족한 방법이 떠오르지 않았다.
해설을 보니 피보나치 풀었던 방법을 제대로 생각하지 못한 것 같다.

해설을 봐도 처음에 이해가 잘 되지 않았다.
연산을 하다가 0이되어버리는 경우는 고려하지 않는 것인지,
숫자에 따라서 이전 숫자에 대한 횟수가 다른 숫자들에 대해 어떤 영향을 주는 직관적으로 와닿지 않았다.
그런데 , 다시 생각해보니  연산을 하다가 어떠한 특정한 숫자가 되었을 때 그값을 기록하고 있다면
그 값을 바로 사용할 수 있다는 것을 이것을 적으면서  생각나게 되었다. 그런데 소스코드가 지금 이해가 가지 않는다.
생각한 것 보다 소스코드가 너무나도 간단하지만 이해가 되지 않는다.
점화식 자체도 이해가 되지 않는다.
소스코드가 엄청나게 간단함에도 아이디어를 떠올릴 수 없었다는 것이 인상깊었고, 분했다.
해설 강의를 듣고 겨우 이해를 할 수 있었고, 많은 문제를 풀어보며 유형에 익숙해지는 것만이 살길이라고 생각을 하게 되었다.


"""
