# condingtest_with_python_part3_구현
# 외벽점검.py



# 나의 풀이 (교재 해설 참고)



# 나의 풀이 (주어진 풀이 시간 : 50분, 풀이 시간 : 분 초)

## 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return하는 함수 완성해라
## 완전탐색으로 풀어보자
## 친구 꺼낼때 시계 반시계 전부 사용해보기
## 시작점은 weak 중 하나에서 시작이고, 끝에서? 근데 아니면 하나씩 다 확인??
##   => weak 중 하나로 하고 하나씩 다 확인해보자!
from itertools import combinations
from itertools import permutations
from itertools import product


def possible(candidates, weak, n):
    start_point_candidates = list(permutations(weak, len(list(candidates[0]))))
    direction_candidates = list(product([1,-1], repeat = len(list(candidates[0]))))
    w = list(range(n))
    
    # 친구 조합들 중 하나를 뽑아서
    for candidate in candidates: # 혹시 얘도 순열 써야 되나???
        # 한 조합을 구성하는 친구 수 만큼 취약 지점들 중 몇 개 뽑아 순서를 고려하여 선정하는 경우들 
        for start_point in start_point_candidates:
            # 시계 방향, 시계 반대 방향 둘 다 봐야 됨
            for direction in direction_candidates:
                temp_weak = weak
                for i in range(len(direction)):
                    s = start_point[i]
                    d = direction[i]
                    c = candidate[i]
                    if d == -1:
                        if s - c < 0:
                            temp_weak = list(set(temp_weak) - set(w[s:-1:-1]))
                            a = n - 1 + (s - c)
                            temp_weak = list(set(temp_weak) - set(w[-1:a:-1]))
                        else:
                            a = s - c - 1
                            temp_weak = list(set(temp_weak) - set(w[s:a:-1]))
                    elif d == 1:
                        if s + c > n - 1:
                            temp_weak = list(set(temp_weak) - set(w[s:]))
                            a = s + c - (n - 1)
                            temp_weak = list(set(temp_weak) - set(w[:a]))
                        else:
                            a = s + c + 1
                            temp_weak = list(set(temp_weak) - set(w[s:a]))       
                # 만약 다 없어졌다면
                if len(temp_weak) == 0:
                    return True
           
    return False

def solution(n, weak, dist):
    for i in range(1, len(dist) + 1):
        candidates = list(combinations(dist, i))
        if possible(candidates, weak, n):
            return i
    return -1
                                
# 교재 풀이
from itertools import permutations

def solution(n, weak, dist):
    # weak 길이 2배로 만들어서 원형을 일자형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입ㅎ살 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    friends = list(permutations(dist, len(dist)))   
    
    # 0부터 length -1 까지의 위치를 가각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friend in friends:
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friend[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 커버할 범위를 벗어난다면(점검할 수 있는 위치를 벗어난다면)
                if position < weak[index]:
                    count += 1 # 새로운 친구 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    # 친구 더 투입하고서 못 닿은 부분부터 다시 시작함
                    position = weak[index] + friend[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer


# 느낀점
"""
정말 시간이 오래 걸렸고, 풀 수 있을 것이라고 생각했음에도 결국에 시간초과를 극복하지 못했다.. 
정말로 어려웠다.. 일단 테시간 초과가 뜬 것 말고는 모두 통과하였다..
코드를 작성하면서도 이렇게 반복문을 중첩하면 아무리 데이터 범위가 작더라도 시간초과가 나오지 않을까
걱정했는데 정말로 그랬다.

1. 해설을 읽어보니 해당 문제처럼 !!!원형으로 나열된 데이터를 처리하는 경우에는, 길이를 2배로 늘려서
'원형'을 일자 형태로 만드는 작업을 해주면 유리하다고 한다!!!

2 .또한 나는 시작점을 무조건 weak 중 하나로 설정하였다. 
그랬음에도 시간초과가 발생하지 않는 다는 것은 내가 작성한 코드에 굉장히 비효율적이었다는 것이다.

3. 나는 permutations->(시작점고르기), combinations->(친구조합고르기), products(시계방향, 반대방향 경우들)
이렇게 세가지 itertools 메서드들을 사용했다.
하지만 교재 풀이는 permutations->(친구조합고르기) 한가지만을 사용했다. 난 친구조합고르는데 combinations을 썼는데
이부분도 달랐다.

4. 교재의 경우 내가 이해한 걸로는 분명 문제에서 역방향으로도 점검할 수 있다고 했음에도 시계 반대방향은
고려하지 않았다.


5. product의 사용법을 제대로 몰랐다. product의 두번 째 매개변수는 'repeat = '를 사용해야된다는 것.


6. 집합으로 만들어 뺴기
"""


