from itertools import permutations
def solution(k, dungeons):
    # 최대 던전수
    # k : 현재 피로도
    # dungeons [[최소 필요 피로도, 소모 피로도]]
    answer = -1
    dungeons = [d for d in dungeons if not k < d[0]]
    candidates = list(permutations(dungeons))
    for candidate in candidates:
        current_k = k
        temp_dungeons = 0
        for c in candidate:
            if current_k < c[0]:
                break
            current_k -= c[1]
            temp_dungeons += 1
        answer = max(answer, temp_dungeons)
    return answer


'''
느낀점 : 
어렵지 않게 풀 수 있었다. 완전탐색을 사용하였는데(itertools의 permutation), 시간초과가 나지 않게 하기 위해
첫 던전의 최소 피로도가 초기 피로도보다 큰 후보는 처음부터 제거하고 시작을 하였고
모든 후보들을 하나씩 읽어들여서 던전을 하나씩 읽어들이고 던전의 최소 피로도 요건이 현재 피로도보다 크다면 바로
continue로 재끼고 다음 후보를 검사하는 방식으로 풀었다.
'''
