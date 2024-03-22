from itertools import permutations

def check_matched(u_id, b_id):
    if len(b_id) != len(u_id):
        return False
    for i in range(len(b_id)):
        if b_id[i] != u_id[i] and b_id[i] != '*':
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    result= []
    candidates = list(permutations(user_id, len(banned_id)))
    #print(candidates)
    for candidate in candidates:
        matched_count = 0
        for i in range(len(banned_id)):
            if check_matched(candidate[i], banned_id[i]):
                matched_count += 1
        if matched_count == len(banned_id):
            result.append(candidate)
    result = set([tuple(set(sorted(candidate))) for candidate in result])
    return len(result)
''' 생각할 점 or 느낀점
user_id와, banned_id의 길이 및 내부 아이디의 길이가 8이하이므로 itertools를 사용하여 가능한 조합들을 구해도 될 것이라고 판단하였다.
처음에는 product를 사용하여 banned_id의 원소들에 대해 각각 매칭되는 user_id들을 구하여 저장한 뒤, 그것에서 하나씩 뽑아 모든 경우의 수를 구하려했다.
하지만 permutation을 사용하면 중복을 허용하지 않는 모든 가능한 경우의 조합을 구할 수 있으며 exact match 여부를 확인하여 정답을 계산할 수 있다.
이러한 문제는 충분히 풀 수 있는 문제이기 때문에, 겁먹지 말고 집중해서 풀면 충분히 제한 시간 내에 풀 수 있을 것이다.
'''

# 카카오이모티콘 이벤트에 비정상적인 방법으로 당첨을 시도한 응모자들을 발견하였습니다. 이런 응모자들을 따로 모아 불량 사용자
# 록을 만들어서 당첨 처리 시 제외하도록 이벤트 당첨자 담당자인 "프로도" 에게 전달
# 개인정보 보호을 위해 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달
# 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 아이디 당 최소 하나 이상의 '*' 문자를 사용
# "무지"와 "프로도"는 불량 사용자 목록에 매핑된 응모자 아이디를 제재 아이디

# 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return
# 순서 상관 없으므로 조합임

# 일단 banned_id 하나씩 읽어들여서 각 banned_id 원소에 대해 매칭 될 수 있는
# user_id를 찾아낸 뒤, 걔의 매칭 될 수 있는 모든 경우의 수를 구하고
# 걔네 들끼리의 조합을 구할까?

''' 합계: 90.9 / 100.0 => 1개 시간초과뜸
from itertools import product
def solution(user_id, banned_id):
    answer = 0
    candidates = []
    for b_id in banned_id:
        temp_candidate = []
        for u_id in user_id:
            if len(b_id) == len(u_id):
                count = 0
                for i in range(len(b_id)):
                    if b_id[i] != u_id[i] and b_id[i] != '*':
                        break
                    else:
                        count += 1
                if count == len(b_id):
                    temp_candidate.append(u_id)
        candidates.append(temp_candidate)         
    
    whole_candidates = list(product(*candidates))
    
    result_candidates = set([tuple(set(sorted(list(candidate)))) for candidate in whole_candidates])
    result_candidates = [candidate for candidate in result_candidates if len(candidate) == len(banned_id)]
    print(result_candidates)
    answer = len(result_candidates)
    return answer
'''
