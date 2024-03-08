# 모든 명함을 수납할 수 있는 가장 작은 지갑의 너비
# [width(너비), height(높이)]
# 모든 조합 중에서 가장 작은애 (너비랑 높이의 순서가 바뀐 것 포함하여)
# sizes의 원소들에 대해 모두 첫번째인덱스 두번째인덱스 swap이 가능하기 때문에
# 모든 sizes의 원소들의 조합의 경우를 보면될듯
# size길이가 만약 4라면 swap, swap안함, swap안함, swap안함
# swap안함, swap, swap, swap 과 같이 조합을 만들어
# 각각에 조합에 대해 최대 너비와 최대 높이의 곱이 가장 작은 애를 구하면됨
# 완전탐색 => itertools
# 명확하게 말하면 조합이 아니라 중복이 가능한 순열이므로 product를 사용해야함
# 완전탐색 문제임에도 완전탐색을 하였더니 시간초과가 떴다.
# 모든 case를 다 비교하지 말고 제일 큰 가로길이를 가진 명함과 제일 큰 세로길이 가진 명함
# 이 두 개에 대해서만 swap를 진행해보면 되는 거 아니야?
# 정답 => 
# 그냥 각 원소안에 두 값은 서로 위치변경이 가능하므로 한쪽으로 큰것들만 몰아 넣고 다른 한쪽으로
# 작은 것들을 몰아 넣은 뒤, 큰 것들중 가장 큰 수, 작은 것들 중 가작 작은 수의 곱을 return하면 끝
def solution(sizes):
    big_things = [size[0] if size[0] > size[1] else size[1] for size in sizes]
    small_things = [size[1] if size[0] > size[1] else size[0] for size in sizes]
    return max(big_things) * max(small_things)

# 더 간단하게 하면
def solution(sizes):
    return max([max(size) for size in sizes]) * max([min(size) for size in sizes])

# 시도했던 것들
## 완전탐색(가로 세로 바꿔보는 것을 (최대너비가진 명함, 최대높이가진 명함)들만 적용)
from itertools import product
from copy import deepcopy
def solution(sizes):
    answer = 1e9
    num = len(sizes)
    # 최대너비인 명함과 최대높이인 명함 찾기
    max_w_idx = []
    max_h_idx = []
    max_width = max([size[0] for size in sizes])
    max_height = max([size[1] for size in sizes])
    for i in range(len(sizes)):
        if sizes[i][0] == max_width:
            max_w_idx.append(i)
        if sizes[i][1] == max_height:
            max_h_idx.append(i)
            
    max_w_max_h_candidates = list(product(max_w_idx, max_h_idx))
    # print(max_w_max_h_candidates)
    for max_w_max_h_candidate in max_w_max_h_candidates:
        for case in [('swap_x', 'swap_x'), ('swap', 'swap_x'),('swap_x', 'swap'),('swap', 'swap'),]:
            temp_sizes = deepcopy(sizes)
            if case[0] == 'swap': # 가로가 최대인 명함의 가로 세로를 swap하는 경우
                temp_sizes[max_w_max_h_candidate[0]][0], temp_sizes[max_w_max_h_candidate[0]][1] =  temp_sizes[max_w_max_h_candidate[0]][1], temp_sizes[max_w_max_h_candidate[0]][0]
            elif case[1] == 'swap': # 세로가 최대인 명함의 가로 세로를 swap하는 경우
        # swap인 애들 가로 세로 길이 바꿈
                temp_sizes[max_w_max_h_candidate[1]][0], temp_sizes[max_w_max_h_candidate[1]][1] =  temp_sizes[max_w_max_h_candidate[1]][1], temp_sizes[max_w_max_h_candidate[1]][0]
            # 가로 중 최대 길이
            max_width = max([size[0] for size in temp_sizes])
            max_height = max([size[1] for size in temp_sizes])
            temp = max_width * max_height
            answer = min(answer, temp)
    return answer

## 완전탐색(가로 세로 바꿔보는 것을 특정 개수(최대너비가진 명함, 최대높이가진 명함)가 아닌 모든 명함들에 대해 적용하여 케이스를 탐색)
from itertools import product
def solution(sizes):
    answer = 1e9
    case = ['swap', 'swap_x']
    number = len(sizes)
    candidates = list(product(case, repeat=number))
    print(candidates)
    for candidate in candidates:
        # swap이라면 가로 세로 길이를 서로 바꿈
        temp_sizes = [[sizes[i][1], sizes[i][0]] if candidate[i] == 'swap' else sizes[i] for i in range(number)] 
        # 가로 중 최대 길이
        max_width = max([size[0] for size in temp_sizes])
        max_height = max([size[1] for size in temp_sizes])
        temp = max_width * max_height
        answer = min(answer, temp)
    return answer
