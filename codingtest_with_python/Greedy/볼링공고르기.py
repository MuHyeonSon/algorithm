# condingtest_with_python_part3_Greedy
# 볼링공고르기.py

# 나의 풀이 (교재 해설 참고)

# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 50분 초)
## 서로 다른 무게가 다른 공을 선택할 거임
## 무게 정보는 리스트로 들어오므로 하나의 값을 선택했을 때, 나올 수 있는 경우의 수는 그 값과 동일한 원소를 제외하고 경우의 수를 구해야 됨
## itertools를 사용하되 그 값을 다 제외한 리스트 내에서 계산해야돼.. 리스트에서 특정값을 갖는 애를 다 지워 버린 뒤 구해야됨
## N의 개수가 1000이므로 그리 크지 않으니 완전탐색으로 ?? 
## 그렇게 하지 말고, combination의 결과 리스트 내의 원소들 하나씩 꺼내서 튜플의 원소값(만약 원소가 5개면 5C2해서)을
##                                        인덱스 값으로 해서 if data[tuple[0]] == data[tuple[1]] : count += 1로 계산할 수 있도록 

import itertools

## 볼링공의 개수 : n , 공의 최대 무게 : m 입력받기
n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
combination_list = list(itertools.combinations(list(range(n)), 2))
for case in combination_list:
    if data[case[0]] != data[case[1]]:
        result += 1
print(result)


"""
for d in data:
    temp_data = copy.deepcopy(data)
    print(f'temp_data : {temp_data}')
    for _ in range(data.count(d)- 1):
        print(f'd : {d}')
        temp_data.remove(d)
        print(f'removed temp_data : {temp_data}')
        #print(f'temp_data : {temp_data}')
    #print(f'temp_data : {temp_data}') 
    number_of_data = len(temp_data)
    cases = list(itertools.combinations(list(range(number_of_data)), 2))
    #print(cases)



data.sort()
temp_data = data
for i in range(1, m + 1):
    temp_index = 0
    for j in range(n):
        if i == j:
            temp_index = 
        and j + 1 < n and j != i:
            

for i in range()
print(len(list(itertools.combinations(data, 2))))

#print(list(range(14)))
"""

# 교재 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

## 1부터 10까지의 무게를 담을 수 있는 리스트 (1 <= m <= 10)
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
    
result = 0
## 1부터 m까지의 각 무게에 대해 처리
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n # B가 선택하는 경우의 수와 해당 차례의 숫자에 개수 곱하기
    
print(result  nm)
 


# 느낀점
"""
문제가 매우 간단해보였지만, 구현이 가능하도록 하는 코드작성에 대한 아이디어를 떠올리는데 시간이 오래걸렸다..
처음에는 복잡하게 생각하여 코드가 엄청길게 작성하며 시도했다가 모두 실패했지만, 최종적으로 구현한 코드는 매우 짧게
작성되었다. 단순하게 볼링공의 개수에서 2개를 뽑는 경우를 모두 구했고 구한 경우들 중 서로 무게가 다른 것만
따로 추출하면 되는 거였는데 너무 복잡하게 생각했던 것 같다.

또한 해설을 읽어보니 나와는 아예 다른 방식으로 푼 것을 알 수 있었다.
자주 느끼는 점이지만 내가 작성한 코드가 해설풀이와 똑같은 결과를 내는지 여러 개의 테스트 케이스를 모두
돌려보고 확인할 수 없다는 점이다.

교재풀이는 라이브러리를 사용하지 않고 경우의 수를 수학적으로 계산하는 방법을 사용하였다.
A와 B가 각각 선택함에 있어서 경우의 수를 따졌는데 아이디어에 대한 구현 법을 정리하면 다음과 같다.

A를 기준으로 무게가 낮은 볼링공부터 무게가 높은 볼링공까지 순서대로 하나씩 확인하는 방법을 사용
5 3 
1 3 2 3 2

-> 1 2 2 3 3
A : 1 B : 2, 2, 3, 3  -> A(무게가 1인 공의 개수 : 1) B(B가 선택하는 경우의 수 : 4) -> 1 * 4 = 4
A : 2 B : 3, 3        -> A(무게가 2인 공의 개수 : 2) B(B가 선택하는 경우의 수 : 2) -> 2 * 2 = 4
A : 3 B :             -> A(무게가 3인 공의 개수 : 2) B(B가 선택하는 경우의 수 : 0) -> 2 * 0 = 2
따라서 답은 8

여기서 B가 선택하는 경우의 수는 줄어드는데 이미 계산했던 경우(조합)는 제외하기 때문이라고 한다.

문제 풀이가 완전히 달라서 검증이된 교재의 풀이를 보고 익히는 수 밖에 없을 것 같다고 생각했다.
"""


