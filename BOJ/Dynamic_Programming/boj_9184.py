#boj 9184 손무현
#재귀함수 호출 방식의 알고리즘을 DP 방식의 알고리즘으로 바꾸는게 문제인 것 같은데
#어떻게 접근해야할까? 
"""
DP
1, 큰 문제 -> 작은 문제 분할
2. 큰 문제의 해 ->작은 해의 점화식
3. DP 테이블 정의
4. 정확성 증명
"""
# 3차원 리스트 생성??...  -> 맞을거야 LCS 계산문제를 떠올려보면 LCS table 채우기 위해 이중 for문 돌렸었잖아? 이거는 3중 for문 돌려서 풀어보자!!!
# w라는 함수는 세가지 매개변수의 조건에 따라 어떠한 출력 값을 계산하여 return 한다.
# 이것을 어떻게 작은 문제로 분할 할 수 있을까??
# w(a,b,c) 얘에 대해 어떠한 공식에 의해 미리 계산된 DP테이블이 있어야 되지 않을까? 그리고 그 DP테이블은 for문을 통해 계속해서 채워지는 형태 ???  
"""
다음과 같은 재귀함수 w(a, b, c)가 있다.


if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:   # 바닥조건??? 실제 인덱스의 범위는 [0,100], a,b,c의 범위는 [-50,50] 따라서 실제 인덱스가 a<=50 or b<=50 or c<=50인 곳은 다 1넣어야 됨
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:   # a > 70 or b > 70 or c > 70 가 성립 되는 위치의 원소는 70,70,70 인덱스 값으로 채워 
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:              # 
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

제한
-50 ≤ a, b, c ≤ 50

예제 입력 1 
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
예제 출력 1 
w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1
"""



def w(a,b,c):
  
input_list = [1,1,1]
while(input_list[0] == -1 and input_list[1] == -1 and input_list[2] == -1):
  global input_list
  input_list = list(map(int,input().split()))

