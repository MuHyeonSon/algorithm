# condingtest_with_python_part3_Greedy
# 만들수없는금액.py

# 교재 해설 풀이
## 동전 개수 입력받기
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    # (현재 리스트에서 읽어들인 금액이 이전까지의 동전들의 합에 1더한 것보다 크다면 만들 수 없음)
    if target < coin:
        break
    else:
        target += coin
## 만들 수 없는 금액 출력
print(target)



# 나의 풀이 (주어진 풀이 시간 : 30분, 풀이 시간 : 못 품)

## 갖고있는 동전으로 만들 없는 금액 중 최솟값 구할 거임 (최소 -> 그리디??)

## 조합은 아닌 것 같아 몇 개 꺼내는지가 그건 몇개꺼내는지가 정해져 있으니까

import itertools

## 동전의 개수 입력받기
n = int(input())

coins = list(map(int, input().split()))

coins.sort() # 오름차순으로 정렬

sum_coins = []

for i in range(1, len(coins) + 1):
    data = list(itertools.combinations(coins,i))
    print(f'data : {data}')
    for d in data:
        if sum(d) not in sum_coins:
            sum_coins.append(sum(d))

min_money = 1000000000
## 포함되어 있지 않으면서 꺼냈을 때 합이 가장 작아야됨 (꺼내는 개수 1부터 하나씩, 꺼내는 수의 합이 작은 거부터)
## 두 원소의 합이 작은 순으로 정렬하는 것은 어떻게 구현할 수 있을까?
for i in range(1, len(coins) + 1):
    data = list(itertools.combinations(coins,i))
    print(f'data : {data}')
    min_data = []
    for d in data:
        print(f' d : {d}')
        min_data.append(sum(d))
    print(f'min_data : {min_data}')    
    min_d = min(min_data) - 1
    if min_d < min_money and min_d >= 1:
        min_money = min_d
print(min_money)


# 느낀점
"""
진심으로 쉬워 보여서 10분안에 풀 수 있을 거라고 생각했는데
결국 구현하지 못했다. 해설읽었는데 이해가 안간다.
두 번째 해설을 읽는 데도 이해가 가지 않는다.

동전을 오름차순으로 정렬 후 하나씩 꺼내서 1로 초기화 했던 'target' 변수보다 현재 꺼낸 동전이 더 크다면
그 target이 답이다. -> 라는 말이 target = 1일 때 일때는 이해가 간다. 가장 첫번째 꺼낸 동전보다 더 작은 값은
없으니 target = 1이 만들 수 없는 가장 작은 값이다.

여기까지는 이해가 갔는데 해설을 보고 이해가 가지 않는 부분은 다음과 같다.

1. 왜 target이 현재 꺼낸 동전 값보다 작다면 그 target 값이 정답인지 이해가 안간다.
    target에는 현재 꺼낸 동전 전까지의 동전값들을 더한 값에 1을 더한 값이다.
    그 1부터 target의 1을 뺸 값까지 다 만들 수 있는 값이라고 한다.
    -> 뭔가 중간에 비는 값들 즉, 만들 수 없는 금액이 존재할 것만 같다.
    얘를 들어 1 1 2 4,7,8가 있고, target이 4까지 읽어들였다면 9인데
    1~8까지 다 만들 수 있어? 1 (1) 2(1+1) 3(1+2) 4(1+1+2) 5(4+1) 6(2+4) 7(2+4+1) 8(1+1+2+4)
    지금 예시하나 들어서 직접해봤는데 진짜 만들 수 있는데 이게 모든 경우의 가능하다는게 와닿지 않고
    맞는 건지 모르겠다.
    만약 7까지 읽어들였다면 16인데 15까지 다만들 수 있나
    1(1) 2(1+1) 3(1+2) 4(1+1+2) 5(4+1) 6(2+4) 7(2+4+1) 8(1+1+2+4) 9(1+1+7) 10(1+2+7) 11(1+1+2+7)
    12(1+4+7) 13(2+4+7) 14(1+2+4+7) 15(1+1+2+4+7)
    진짜 다 만들어지네..  직접 만들어봐도 이게 왜 가능한지 이해가 안간다.
    
해설에서 해당 문제는 그리디 알고리즘 유형의 문제를 여러 번 풀어보았다면 풀이 방법을 떠올 릴 수 있지만,
그리디 알고리즘이 익숙하지 않다면 쉽게 이해되지 않을 수 있는 문제라고 한다. 따라서 이 문제가 어렵다면 그리디 알고리즘
유형의 문제를 더욱 많이 접해봐야된다고 한다.

또한 앞의 이론파트에서 나왔던 거스름돈 문제와 다른 점은 그 문제는 각 화폐 단위마다 무한 개의 동전이
존재한다고 가정했지만, 여기서는 동전의 수가 한정적이라는 다른 점이 존재한다.
"""
"""
