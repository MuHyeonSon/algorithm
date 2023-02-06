# condingtest_with_python_part3_DynamicProgramming
# 못생긴수.py

# 나의 풀이 (교재 해설 참고)


# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 28분 51초 )

## 못생긴수 : 오직 2, 3, 5를 소인수로 가지는 수를 의미(2,3,5를 약수로 가지는 합성수)
## 1: 못생긴 수 로 가정
## 못생긴수 집합 = {1,2,3,4,5,6,8,9,10,12,15}
## n번째 못생긴 수를 찾는 프로그램을 작성하라 (11번쨰 못생긴 수는 15다.)
## 어떻게 해야될까?
## 2,3,5를 약수로 가진다면 2,3,5의 배수들도 모두 못생긴 수 인데,  몇 번째인지 구하려면 어떻게 해야될까
## 1 <= n <= 1000이니까 DP테이블을 먼저 만들어?
## DP는 작은 해들이 모여 큰 해가 되니까

n = int(input()) # n번째 못생긴 수를 찾을 때의 n을 입력받음
dp = [0, 1]
count = 0
index = 1
if n == 1:
    print(1)    
else:
    while True:
        dp.append(dp[index] * 2)
        count += 1
        dp.append(dp[index] * 3)
        count += 1
        dp.append(dp[index] * 3)
        count += 1         
        if count >= n:
            dp.sort()
            print(dp[n])
            break
        else:
            index += 1
        


# 교재 풀이

# 느낀점
"""
"""

"""
📰 Codingtest_with_python_part3_DynamicProgramming_못생긴수
"이것이취업을위한코딩테스트다" 학습 순서 3단계
Part3 기출문제 DynamicProgramming 문제 풀이 느낀점
"""
