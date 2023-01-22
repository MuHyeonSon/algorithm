# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return하는 함수 완성해라
# 완전탐색으로 풀어보자
# 친구 꺼낼때 시계 반시계 전부 사용해보기
# 시작점은 weak 중 하나에서 시작이고, 끝에서? 근데 아니면 하나씩 다 확인??
#   => weak 중 하나로 하고 하나씩 다 확인해보자!
from itertools import combinations
from itertools import permutations
from itertools import product


def possible(candidates, weak, n):
    start_point_candidates = list(permutations(weak, len(candidates[0])))
    direction_candidates = list(product([1,-1], repeat = len(candidates[0])))
    w = list(range(min(weak), max[weak] + 1))
    # 친구 조합들 중 하나를 뽑아서
    for candidate in candidates: ## 혹시 얘도 순열 써야 되나???
        # 한 조합을 구성하는 친구 수 만큼 취약지점들 중 몇 개뽑아 순서를 고려하여 선정하는 경우들   
        for start_point in start_point_candidates:
            # 시계 방향, 시계 반대 방향 둘 다 봐야됨
            for direction in direction_candidates:
                temp_weak = weak
                for i in range(len(direction)):
                    s = start_point[i]
                    d = direction[i]
                    c = candidate[i]
                    if d == -1:
                        if s - c < 0:
                            temp_weak = list(set(temp_weak) - set(weak[s:-1:-1]))
                            temp_weak = list(set(temp_weak) - set(weak[-1:-(n-(c-s)):-1]))
                        else:
                            temp_weak = list(set(temp_weak) - set(weak[s:s-c-1,-1]))
                    else:
                        if s + c > n:
                            temp_weak = list(set(temp_weak) - set(weak[s:]))
                            temp_weak = list(set(temp_weak) - set(weak[:n - (s+c) + 1]))
                        else:
                            temp_weak = list(set(temp_weak) - set(weak[s:s+c+1]))
            # 만약 다 없어졌다면
            if len(temp_weak) == 0:
                return True            
    return False

def solution(n, weak, dist):
    for i in range(1, len(dist)):
        candidates = list(combinations(dist, i))
        if possible(candidates, weak, n):
            return i
    return len(weak)
                                
                                
                        
"""
        for i in range(len(len(candidate[0])):
            start_point = start_point_candidates[i]
            direction = direction_candidates[i]    
"""
